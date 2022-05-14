from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from habibas_blog.accounts.models import Profile
from habibas_blog.core.models import Comment, Post, CommentLike

UserModel = get_user_model()


class TestProfileDetailsView(TestCase):
    # SETUPS
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

    @staticmethod
    def __create_post():
        post = Post.objects.create(title='simple test title',
                                   catchy_title='simple catchy title',
                                   image_url='http://www.wallpaper.com/1',
                                   content='Lorem Ipsum my dear',
                                   status=1)
        return post

    @staticmethod
    def __create_post_comment(post, user):
        comment = Comment.objects.create(content='lorrem ipsum my dear i am a professional troll',
                                         post=post,
                                         user_id=user
                                         )
        return comment

    @staticmethod
    def __create_comment_like(user, comment):
        comment_like = CommentLike.objects.create(user=user,
                                                  comment=comment)
        return comment_like

    # ACTUAL TESTS
    def test_view_uses_correct_template(self):
        user = self.__create_user()
        response = self.client.post(reverse('profile-details', kwargs={'pk': user.id}))
        self.assertTemplateUsed('accounts/profile-details.html')

    def test_view_shows_correct_user(self):
        user = self.__create_user()
        self.client.login(email='test@mail.com', password='4567gopnik')
        profile = self.__create_profile(user)
        response = self.client.get(reverse('profile-details', kwargs={'pk': user.id}))
        profile_shown = response.context['profile']
        self.assertEqual(profile_shown, profile)

    def test_profile_has_correct_comments_count(self):
        user = self.__create_user()
        self.client.login(email='test@mail.com', password='4567gopnik')
        profile = self.__create_profile(user)
        post = self.__create_post()
        comment = self.__create_post_comment(post, user)
        profile_comments_count = len(Comment.objects.filter(user_id=user.id))

        self.assertEqual(profile_comments_count, 1)

    def test_profile_has_correct_comment_likes_count(self):
        user = self.__create_user()
        self.client.login(email='test@mail.com', password='4567gopnik')
        profile = self.__create_profile(user)
        post = self.__create_post()
        comment = self.__create_post_comment(post, user)
        comment_like = self.__create_comment_like(user, comment)
        comment_likes_count = comment.likes_count()

        self.assertEqual(comment_likes_count, 1)

    def test_view_shows_correct_comments_in_section(self):
        user = self.__create_user()

        self.client.login(email='test@mail.com', password='4567gopnik')
        profile = self.__create_profile(user)
        post = self.__create_post()
        comment = self.__create_post_comment(post, user)

        user_2 = UserModel.objects.create_user(email='test2@mail.com', password='456789gopnik')
        profile_2 = Profile.objects.create(first_name='test',
                                         last_name='testov',
                                         dob='1988-12-12',
                                         gender='male',
                                         phone='1234534455',
                                         user=user_2,)
        comment_2 = Comment.objects.create(content='lorrem ipsum my dear i am a professional troll',
                                         post=post,
                                         user_id=user_2)
        self.assertNotEqual(comment.user_id, comment_2.user_id)
        self.assertEqual(comment.user_id, user)

