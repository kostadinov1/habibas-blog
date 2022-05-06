from django.urls import path

from habibas_blog.core.views.generic import HomeView, build_elements_page, ContactsView
from habibas_blog.core.views.posts import BlogView, single_post_view

urlpatterns = (
    path('', HomeView.as_view(), name='home'),
    path('blog/', BlogView.as_view(), name='blog'),
    path('single-blog/<int:pk>', single_post_view, name='single blog'),
    path('elements/', build_elements_page, name='elements'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
)