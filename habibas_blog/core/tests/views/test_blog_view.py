from django.test import TestCase
from django.urls import reverse

from habibas_blog.core.models import Post


class TestBlogView(TestCase):

    @staticmethod
    def __create_post(title, status_code):
        post = Post.objects.create(title=title,
                                   catchy_title='simple catchy title',
                                   image_url='http://www.wallpaper.com/1',
                                   content='Lorem Ipsum my dear',
                                   status=status_code)
        post.save()
        return post

    def test_view_shows_published_posts_only(self):
        post_published = self.__create_post('simple post', 1)
        post_draft = self.__create_post('simple post 2', 0)

        response = self.client.get(reverse('blog'))
        post_shown = response.context['posts'][0]
        self.assertEqual(post_shown, post_published)

    def test_view_shows_correct_2_last_viewed_posts(self):
        pass


