from django.shortcuts import render
from django.views.generic import TemplateView, DetailView

from habibas_blog.core.models import Post


class HomeView(TemplateView):
    template_name = 'core/index.html'

    def get_context_data(self, **kwargs):
        posts = Post.objects.all()

        context = super().get_context_data(**kwargs)
        context['posts'] = posts

        return context


class ContactsView(TemplateView):
    template_name = 'core/contacts.html'



    # def get_queryset(self):
    #     return super().get_queryset().prefetch_related('tagged_posts')



def build_elements_page(request):
    return render(request, 'elements.html')


