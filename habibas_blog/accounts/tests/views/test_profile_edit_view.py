from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse, reverse_lazy

from habibas_blog.accounts.models import Profile

UserModel = get_user_model()


class TestProfileEditView(TestCase):

    @staticmethod
    def __create_user():
        user = UserModel.objects.create_user(email='test@mail.com',
                                             password='4567gopnik')
        return user

    @staticmethod
    def __create_profile(user):
        profile = Profile.objects.create(first_name='test',
                                         last_name='testov',
                                         dob='1988-12-12',
                                         gender='male',
                                         phone='1234345345',
                                         user=user, )
        return profile

    def test_uses_correct_template(self):
        user = self.__create_user()
        response = self.client.post(reverse('profile-edit', kwargs={'pk':user.id}))
        self.assertTemplateUsed('accounts/profile-edit.html')

# TODO THIS ONE NEEDS TO HAVE ANOTHER LOOK
    def test_redirects_to_correct_template_on_success(self):
        user = self.__create_user()
        self.client.login(email='test@mail.com', password='4567gopnik')
        profile = self.__create_profile(user)
        profile_data = {'first_name': 'test',
                        'last_name': 'testovian',
                        'dob': '1988-12-12',
                        'gender': 'male',
                        'phone': '1234345345',
                        'user': user}

        response = self.client.post(reverse('profile-edit', kwargs={'pk': user.id}),
                                    data=profile_data)
        self.assertRedirects(response, f'/profile-details/{profile.user.id}/')

    def test_edit_profile_successfully(self):
        user = self.__create_user()
        self.client.login(email='test@mail.com', password='4567gopnik')
        profile = self.__create_profile(user)
        edited_profile = {'first_name': 'test',
                          'last_name': 'testovski',
                          'dob': '1988-12-12',
                          'gender': 'male',
                          'phone': '1234345345',
                          'user': user,
                          }

        response = self.client.post(reverse('profile-edit', kwargs={'pk': profile.user.id}),
                                    data=edited_profile)
        result = response.context['profile']
        self.assertEqual(result.last_name, 'testovski')


