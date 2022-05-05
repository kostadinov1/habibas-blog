from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView

from habibas_blog.accounts.forms import UserRegistrationForm
from habibas_blog.accounts.models import Profile


class UserRegistrationView(CreateView):
    form_class = UserRegistrationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        return result

class UserLoginView(LoginView):
    template_name = 'accounts/login.html'

    def get_success_url(self):
        return reverse_lazy('home')


@login_required
def build_logout(request):
    logout(request)
    # messages.info(request, 'LOG OUT SUCCESSFUL')
    return redirect('home')

class ChangePasswordView(PasswordChangeView, LoginRequiredMixin):
    success_url = reverse_lazy('login')



class ProfileDetailsView(DetailView):
    template_name = 'accounts/profile-details.html'
    model = Profile
    context_object_name = 'profile'
