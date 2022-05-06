from django.http import Http404
from django.shortcuts import render
from django.views.generic import DetailView, ListView, TemplateView

from habibas_blog.core.models import Post, Comment


class BlogView(ListView):
    template_name = 'core/index.html'
    model = Post
    context_object_name = 'posts'


def single_post_view(request, pk):
    post = Post.objects.get(pk=pk)
    comments = Comment.objects.filter(post_id=post.pk)



    context = {
        'post': post,
        'comments': comments
    }
    return render(request, 'core/single.html', context)


# TODO HOW TO GET THE PK OF THE REQUESTED OBJECT IN DetailView ----> ?!?!?!
# class SinglePostView(DetailView):
#     model = Post
#     template_name = 'core/single.html'
#     context_object_name = 'post'
#
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         post_pk = context['post']
#         comments = Comment.objects.get(post_id=post_pk.pk)
#         context['comments'] = comments