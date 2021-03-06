from django.contrib.auth import get_user_model
from django.test import TestCase

from habibas_blog.accounts.models import Profile
from habibas_blog.core.models import CommentLike, Comment, Post

UserModel = get_user_model()


class TestCommentLikes(TestCase):


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
    def test_comment_likes_count_correct(self):
        user = self.__create_user()
        post = self.__create_post('simple post title')
        comment = self.__create_post_comment(post, user)
        comment_like_1 = self.__create_comment_like(user, comment)
        comment_like_2 = self.__create_comment_like(user, comment)
        comment_likes_count = comment.likes_count()
        self.assertEqual(comment_likes_count, 2)