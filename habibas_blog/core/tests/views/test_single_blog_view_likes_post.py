from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from habibas_blog.accounts.models import Profile
from habibas_blog.core.models import Post, Comment, CommentLike

UserModel = get_user_model()


class SingleBlogViewPostLikes(TestCase):

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
    def test_user_can_like_post_only_once(self):
        user = self.__create_user()
        self.client.login(email='test@mail.com', password='4567gopnik')
        profile = self.__create_profile(user)
        post = self.__create_post('simple post title')
        post_like = {'user': user,
                     'post': post}
        post_like_response = self.client.post(reverse('like post', kwargs={'pk': post.id}), data=post_like)

        post_like_2 = {'user': user,
                       'post': post}
        post_like_response_2 = self.client.post(reverse('like post', kwargs={'pk': post.id}), data=post_like_2)
        # post_likes = post_like_response_2.context['post'].likes_count()
        post_likes = post.likes_count()
        self.assertEqual(post_likes, 1)

    def test_correct_redirect_after_post_like(self):
        user = self.__create_user()
        self.client.login(email='test@mail.com', password='4567gopnik')
        profile = self.__create_profile(user)
        post = self.__create_post('simple post title')
        post_like = {'user': user,
                     'post': post}
        post_like_response = self.client.post(reverse('like post', kwargs={'pk': post.id}), data=post_like)

        self.assertRedirects(post_like_response, f'/single-blog/{post.id}')
