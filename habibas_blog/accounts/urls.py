from django.urls import path

from habibas_blog.accounts.views import UserRegistrationView, UserLoginView, build_logout

urlpatterns = (

    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', build_logout, name='logout')

)