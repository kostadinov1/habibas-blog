from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from habibas_blog.accounts.models import Profile
from habibas_blog.core.models import Post, Comment, CommentLike

UserModel = get_user_model()


class TestSingleBlogView(TestCase):

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

    def test_view_shows_correct_post(self):
        post = self.__create_post()
        response = self.client.get(reverse('single post', kwargs={'pk': post.id}))
        post_shown = response.context['post']
        self.assertEqual(post_shown, post)

    def test_view_adds_comment_correctly(self):
        user = self.__create_user()
        self.client.login(email='test@mail.com', password='4567gopnik')
        profile = self.__create_profile(user)
        post = self.__create_post('simple post title')
        comment = {'content': 'lorrem ipsum my dear i am a professional troll',
                   'post': post,
                   'user_id': user
                }
        response = self.client.post(reverse('single post', kwargs={'pk': post.id}), data=comment)
        comment_added = Comment.objects.filter(post_id=post.pk)[0]
        self.assertEqual(comment_added.post, post)

    def test_shows_only_relevant_post_comments(self):
        user = self.__create_user()
        self.client.login(email='test@mail.com', password='4567gopnik')
        profile = self.__create_profile(user)
        post = self.__create_post('post1')
        post_2 = self.__create_post('post2')
        comment = self.__create_post_comment(post, user)
        comment_2 = self.__create_post_comment(post_2, user)
        response = self.client.get(reverse('single post', kwargs={'pk': post.id}))
        comment_added = response.context['comments']
        self.assertNotEqual(comment_added, comment_2)
        post_comment = Comment.objects.filter(post_id=post.pk)[0]
        self.assertEqual(post_comment, comment)

    def test_shows_correct_num_post_likes(self):
        user = self.__create_user()
        self.client.login(email='test@mail.com', password='4567gopnik')
        profile = self.__create_profile(user)
        post = self.__create_post('post1')
        comment = self.__create_post_comment(post, user)
        like_comment = self.__create_comment_like(user, comment)

        response = self.client.post(reverse('single post', kwargs={'pk': post.id}))
        comment_added = response.context['comments'][0]
        self.assertEqual(comment_added.likes_count(), comment.likes_count())

    def test_adds_post_to_session_last_viewed_posts_middleware(self):
        user = self.__create_user()
        self.client.login(email='test@mail.com', password='4567gopnik')
        profile = self.__create_profile(user)
        post = self.__create_post('post1')

        response = self.client.post(reverse('single post', kwargs={'pk': post.id}))
        last_viewed_post_pk = self.client.session['last_viewed_posts'][0]
        last_viewed_post = Post.objects.get(pk=last_viewed_post_pk)
        self.assertEqual(last_viewed_post, post)

    def test_view_redirects_to_correct_template_when_no_profile(self):
        post = self.__create_post('simple post')
        response = self.client.post(reverse('single post', kwargs={'pk': post.id}))
        self.assertRedirects(response, '/accounts/profile-create/')

    def test_view_redirects_to_correct_template_after_adding_comment(self):
        user = self.__create_user()
        self.client.login(email='test@mail.com', password='4567gopnik')
        profile = self.__create_profile(user)
        post = self.__create_post('simple post')
        comment = {'content': 'lorrem ipsum my dear i am a professional troll',
                   'post': post,
                   'user_id': user
                   }
        response = self.client.post(reverse('single post', kwargs={'pk': post.id}), data=comment)
        self.assertRedirects(response, '/single-blog/1')

