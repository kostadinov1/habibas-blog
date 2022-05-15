import tempfile

from django.test import TestCase
from django.urls import reverse

from habibas_blog.core.models import ImageGallery



class TestGalleyView(TestCase):

    IMAGE = tempfile.NamedTemporaryFile(suffix=".jpg").name

    def test_gallery_shows_6_items_on_page(self):
        pass

    def test_gallery_shows_correct_queryset(self):
        images = ImageGallery.objects.create(title='image1',
                                             local_image=self.IMAGE)
        response = self.client.get(reverse('gallery'))
        image_shown = response.context['images'][0]
        self.assertEqual(image_shown, images)

    def test_gallery_user_correct_cover_image(self):
        images = ImageGallery.objects.create(title='image1',
                                             local_image=self.IMAGE,
                                             cover_image=True)
        response = self.client.get(reverse('gallery'))
        image_shown = response.context['cover_image']
        self.assertEqual(image_shown, images.local_image)
