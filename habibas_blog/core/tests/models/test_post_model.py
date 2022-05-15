from django.contrib.auth import get_user_model
from django.test import TestCase

from habibas_blog.accounts.models import Profile
from habibas_blog.core.models import CommentLike, Comment, Post, PostLike

UserModel = get_user_model()


class TestPostModelMethods(TestCase):


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
                                         user=user, )
        return profile

    @staticmethod
    def __create_post(title):
        post = Post.objects.create(title=title,
                                   catchy_title='simple catchy title',
                                   image_url='http://www.wallpaper.com/1',
                                   content='Lorem Ipsum my dear',
                                   status=1)
        return post

    @staticmethod
    def __create_post_like(user, post):
        post_like = PostLike.objects.create(user=user,
                                            post=post)
        return post_like

    @staticmethod
    def __create_post_comment(post, user):
        comment = Comment.objects.create(content='lorrem ipsum my dear i am a professional troll',
                                         post=post,
                                         user_id=user
                                         )
        return comment


    # ACTUAL TESTS
    def test_post_likes_count_correct(self):
        user = self.__create_user()
        post = self.__create_post('simple post title')
        post_like_1 = self.__create_post_like(user, post)
        post_like_2 = self.__create_post_like(user, post)
        post_likes_count = post.likes_count()
        self.assertEqual(post_likes_count, 2)

    def test_post_comments_count_correct(self):
        user = self.__create_user()
        post = self.__create_post('simple post title')
        post_comment_1 = self.__create_post_comment(post, user)
        post_comment_2 = self.__create_post_comment(post, user)
        post_comments_count = post.comments_count()
        self.assertEqual(post_comments_count, 2)
