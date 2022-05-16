from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView

from habibas_blog.core.forms import CommentForm
from habibas_blog.core.models import Post, Comment, PostLike, CommentLike, BlogOwner


class BlogView(ListView):
    template_name = 'core/index.html'
    model = Post
    published_posts = Post.objects.filter(status='1')

    queryset = published_posts
    context_object_name = 'posts'
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['owner'] = BlogOwner.objects.first()

        last_viewed_posts = self.request.session.get('last_viewed_posts')
        if last_viewed_posts:
            last_viewed_posts = [Post.objects.get(pk=pk) for pk in last_viewed_posts]
            context['last_viewed_posts'] = last_viewed_posts[:2]
        return context


def single_post_view(request, pk):
    owner = BlogOwner.objects.first()
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return reverse('404')

    comments = list(Comment.objects.filter(post_id=post.pk))
    like = list(PostLike.objects.filter(post_id=post.pk, user_id=request.user.id))
    post_liked = len(like) > 0
    # middleware helper
    viewed_posts = request.session.get('last_viewed_posts', [])
    viewed_posts.insert(0, pk)
    request.session['last_viewed_posts'] = viewed_posts[:4]

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
        'owner': owner,
        'post_liked': post_liked,
        'post': post,
        'comments': comments,
        'form': form,

    }
    return render(request, 'core/single.html', context)


@login_required
def like_post(request, pk):
    post = Post.objects.get(pk=pk)
    like_check = PostLike.objects.filter(user_id=request.user.id)
    if not like_check:
        like = PostLike.objects.create(user_id=request.user.id, post_id=post.id)
        like.save()
    else:
        pass
    return redirect('single post', post.pk)


@login_required
def like_comment(request, pk):
    comment = Comment.objects.get(pk=pk)
    like_check = CommentLike.objects.filter(user_id=request.user.id, comment_id=comment.id).distinct()
    if not like_check:
        like = CommentLike.objects.create(user_id=request.user.id, comment_id=comment.id)
        like.save()
    else:
        pass
    return redirect('single post', comment.post.pk)

# old cb detail view

# class SinglePostView(DetailView):
#     model = Post
#     template_name = 'core/single.html'
#     context_object_name = 'post'
#
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         post_pk = context['post']
#         comments = Comment.objects.get(post_id=self.kwargs['pk'])
#         context['comments'] = comments