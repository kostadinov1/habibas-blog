from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, DetailView, ListView

from habibas_blog.core.forms import ContactForm
from habibas_blog.core.models import Post, ImageGallery, OwnerArticle


class HomeView(ListView):
    template_name = 'core/home.html'
    paginate_by = 2
    model = OwnerArticle
    ordering = '-created_on'
    context_object_name = 'articles'

    def get_context_data(self, **kwargs):
        cover_image = OwnerArticle.objects.filter(cover_image=True)
        context = super().get_context_data(**kwargs)
        if cover_image:
            context['cover_image'] = cover_image[0].image
        return context


class GalleryView(ListView):
    template_name = 'core/gallery.html'
    paginate_by = 6
    model = ImageGallery
    ordering = '-created_on'
    context_object_name = 'images'

    def get_context_data(self, **kwargs):
        cover_image = ImageGallery.objects.filter(cover_image=True)
        context = super().get_context_data(**kwargs)
        if cover_image:
            context['cover_image'] = cover_image[0].local_image

        return context


def contacts_view(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            name = cleaned_data.get('name')
            email = cleaned_data.get('email')
            message = cleaned_data.get('message')
            send_mail(f'New BlogPost message from {name}', message=message, from_email=email, recipient_list=['somemail@mail.com'])
            return redirect('home')

    context = {
        'form': form,
    }
    return render(request, 'core/contacts.html', context)


def build_elements_page(request):
    return render(request, 'elements.html')


