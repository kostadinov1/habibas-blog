from django.http import Http404
from django.shortcuts import render, redirect
from django.views.generic import DetailView, ListView, TemplateView

from habibas_blog.core.forms import CommentForm
from habibas_blog.core.models import Post, Comment


class BlogView(ListView):
    template_name = 'core/index.html'
    model = Post
    context_object_name = 'posts'


def single_post_view(request, pk):
    post = Post.objects.get(pk=pk)
    comments = Comment.objects.filter(post_id=post.pk)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        try:
            profile = request.user.profile
        except Exception:
            return redirect('profile-create')

        if form.is_valid():
            form = form.save(commit=False)
            form.user_id = request.user
            form.post = post
            form.save()
            return redirect('single post', post.pk)
    else:
        form = CommentForm()
    context = {
        'post': post,
        'comments': comments,
        'form': form,

    }
    return render(request, 'core/single.html', context)

#
def like_comment(request, pk):

    comment = Comment.objects.get(pk=pk)
    comment.likes += 1
    comment.save()
    return redirect('single post', comment.post.pk)


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