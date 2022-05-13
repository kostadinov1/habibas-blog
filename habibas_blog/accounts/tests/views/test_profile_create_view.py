from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from habibas_blog.accounts.models import Profile

UserModel = get_user_model()


class TestProfileCreateView1(TestCase):

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
        response = self.client.post(reverse('profile-create'))
        self.assertTemplateUsed('accounts/profile-create.html')

    def test_profile_gets_created_in_db(self):
        user = self.__create_user()
        self.client.login(email='test@mail.com', password='4567gopnik')
        profile = {'first_name': 'test',
                   'last_name': 'testov',
                   'dob': '1988-12-12',
                   'gender': 'Male',
                   'phone': '1234345345',
                   'user': user
        }
        response = self.client.post(reverse('profile-create'), data=profile)
        result = Profile.objects.first()
        self.assertIsNotNone(result)
        self.assertEqual(type(result), Profile)

    def test_view_redirects_to_correct_template_on_success(self):
        user = self.__create_user()
        self.client.login(email='test@mail.com', password='4567gopnik')
        profile = {'first_name': 'test',
                   'last_name': 'testov',
                   'dob': '1988-12-12',
                   'gender': 'Male',
                   'phone': '1234345345',
                   'user': user
        }

        response = self.client.post(reverse('profile-create'), data=profile)
        self.assertRedirects(response, '/')

    def test_create_profile__when_valid_expect_success(self):
        user = UserModel.objects.create_user(email='evga@mail.com',
                                        password='7890plioK')
        self.client.login(email='evga@mail.com', password='7890plioK')

        profile_info = {'first_name': 'evgeni',
                        'last_name': 'testov',
                         'dob': '1987-12-12',
                        'gender': 'Male',
                        'phone': '123543534',

                        'user': user
                        }
        self.client.post(reverse('profile-create'), data=profile_info)
        profile = Profile.objects.first()
        print(profile)
        self.assertIsNotNone(profile)
        self.assertEqual(profile.first_name, 'evgeni')
        self.assertEqual(profile.last_name, 'testov')

    def test_create_profile__when_NOT_valid_expect_fails(self):
        user = UserModel.objects.create_user(email='evga@mail.com',
                                        password='7890plioK')
        self.client.login(email='evga@mail.com', password='7890plioK')

        profile_info = {'first_name': 'evgeni',
                        'last_name': 'testo23v',
                         'dob': '1987-12-12',
                        'gender': 'Male',
                        'phone': '123543534',

                        'user': user
                        }
        self.client.post(reverse('profile-create'), data=profile_info)
        profile = Profile.objects.first()
        print(profile)
        self.assertIsNone(profile)