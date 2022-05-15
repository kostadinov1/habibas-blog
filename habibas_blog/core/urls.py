from django.urls import path

from habibas_blog.accounts.views import ChangePasswordView, build_404_view
from habibas_blog.core.views.generic import HomeView, build_elements_page, contacts_view, GalleryView
from habibas_blog.core.views.posts import BlogView, single_post_view, like_comment, like_post

urlpatterns = (
    path('', HomeView.as_view(), name='home'),
    path('gallery', GalleryView.as_view(), name='gallery'),
    path('blog/', BlogView.as_view(), name='blog'),
    path('single-blog/<int:pk>', single_post_view, name='single post'),
    path('like-post/<int:pk>', like_post, name='like post'),
    path('like-comment/<int:pk>', like_comment, name='like comment'),
    path('elements/', build_elements_page, name='elements'),
    path('contacts/', contacts_view, name='contacts'),
    path('change-password/', ChangePasswordView.as_view(), name='change password'),
    path('404/', build_404_view, name='404')
)