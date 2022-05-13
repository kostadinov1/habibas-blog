from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from habibas_blog.accounts.models import Profile

UserModel = get_user_model()


class ProfileDeleteViewTest(TestCase):

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
                                         user=user,)
        return profile

    def test_view_uses_correct_template(self):
        user = self.__create_user()
        profile = self.__create_profile(user)
        response = self.client.post(reverse('profile-delete', kwargs={'pk':user.id}))
        self.assertTemplateUsed('accounts/profile-delete.html')

    def test_view_redirects_to_correct_template_on_success(self):
        user = self.__create_user()
        self.client.login(email='test@mail.com', password='4567gopnik')
        profile = self.__create_profile(user)
        response = self.client.post(reverse('profile-delete', kwargs={'pk': user.id}))
        self.assertRedirects(response, '/')

    def test_user_and_profile_deleted_successful(self):
        user = self.__create_user()
        self.client.login(email='test@mail.com', password='4567gopnik')
        profile = self.__create_profile(user)

        response = self.client.post(reverse('profile-delete', kwargs={'pk': user.id}))
        result = Profile.objects.first()
        self.assertIsNone(result)