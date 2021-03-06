from django.urls import path

from habibas_blog.accounts.views import UserRegistrationView, UserLoginView, build_logout, ProfileDetailsView, \
    ProfileCreateView, ProfileEditView, ProfileDeleteView

urlpatterns = (

    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', build_logout, name='logout'),
    path('profile-details/<int:pk>/', ProfileDetailsView.as_view(), name='profile-details'),
    path('profile-create/', ProfileCreateView.as_view(), name='profile-create'),
    path('profile-edit/<int:pk>', ProfileEditView.as_view(), name='profile-edit'),
    path('profile-delete/<int:pk>', ProfileDeleteView.as_view(), name='profile-delete'),


)