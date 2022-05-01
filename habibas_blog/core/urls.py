from django.urls import path

from habibas_blog.core.views.generic import HomeView, SinglePostView, build_elements_page

urlpatterns = (
    path('', HomeView.as_view(), name='home'),
    path('single-blog/<int:pk>', SinglePostView.as_view(), name='single blog'),
    path('elements/', build_elements_page, name='elements'),
)