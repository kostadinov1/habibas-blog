from django.shortcuts import render
from django.views.generic import TemplateView, DetailView

from habibas_blog.core.models import Post, ImageGallery


class HomeView(TemplateView):
    template_name = 'core/home.html'

    def get_context_data(self, **kwargs):
        images = ImageGallery.objects.all()
        cover_image = ImageGallery.objects.filter(cover_image=True)

        context = super().get_context_data(**kwargs)
        context['images'] = images
        if cover_image:
            context['cover_image'] = cover_image[0].local_image

        return context


class ContactsView(TemplateView):
    template_name = 'core/contacts.html'


def build_elements_page(request):
    return render(request, 'elements.html')


