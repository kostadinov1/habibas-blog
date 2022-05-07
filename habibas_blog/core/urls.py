from django.urls import path

from habibas_blog.core.views.generic import HomeView, build_elements_page, ContactsView
from habibas_blog.core.views.posts import BlogView, single_post_view, like_comment

urlpatterns = (
    path('', HomeView.as_view(), name='home'),
    path('blog/', BlogView.as_view(), name='blog'),
    path('single-blog/<int:pk>', single_post_view, name='single post'),
    path('like-comment/<int:pk>', like_comment, name='like comment'),
    path('elements/', build_elements_page, name='elements'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
)