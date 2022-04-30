from django.urls import path

from habibas_blog.core.views.generic import HomeView, SinglePostView

urlpatterns = (
    path('', HomeView.as_view(), name='home'),
    path('single-blog/<int:pk>', SinglePostView.as_view(), name='single blog'),


)