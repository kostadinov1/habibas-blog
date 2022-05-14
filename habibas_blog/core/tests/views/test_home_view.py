import tempfile

from django.test import TestCase
from django.urls import reverse

from habibas_blog.core.models import OwnerArticle


class TestHomeView(TestCase):

    IMAGE = tempfile.NamedTemporaryFile(suffix=".jpg").name

    def test_home_shows_correct_articles(self):
        articles = OwnerArticle.objects.create(title='article1',
                                               image=self.IMAGE,
                                               content='lorem ipsum')
        response = self.client.get(reverse('home'))
        article_shown = response.context['articles'][0]
        self.assertEqual(article_shown, articles)

    def test_home_shows_correct_article_cover_image(self):
        articles = OwnerArticle.objects.create(title='article1',
                                               image=self.IMAGE,
                                               content='lorem ipsum',
                                               cover_image=True)
        response = self.client.get(reverse('home'))
        article_shown = response.context['cover_image']
        self.assertEqual(article_shown, articles.image)


