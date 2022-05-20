from django.contrib.auth import login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordChangeDoneView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from habibas_blog.accounts.forms import UserRegistrationForm, ProfileCreateForm, ProfileEditForm, ProfileDeleteForm
from habibas_blog.accounts.models import Profile
from habibas_blog.core.models import Comment

UserModel = get_user_model()


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
    return redirect('home')


class ChangePasswordView(PasswordChangeView, LoginRequiredMixin):
    success_url = reverse_lazy('login')


class ChangePasswordDoneView(PasswordChangeDoneView):
    template_name = 'accounts/login.html'


class ProfileDetailsView(DetailView):
    template_name = 'accounts/profile-details.html'
    model = Profile
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        comments = Comment.objects.filter(user_id=self.request.user.id)
        comments_count = len(comments)
        likes_count = 0
        for comment in comments:
            likes_count += comment.likes_count()

        context['likes_count'] = likes_count
        context['comments_count'] = comments_count
        context['comments'] = comments
        return context


class ProfileCreateView(CreateView, LoginRequiredMixin):
    template_name = 'accounts/profile-create.html'
    model = Profile
    form_class = ProfileCreateForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ProfileEditView(UpdateView, LoginRequiredMixin):
    model = Profile
    template_name = 'accounts/profile-edit.html'
    form_class = ProfileEditForm
    context_object_name = 'profile'

    def get_success_url(self):
        return reverse_lazy('profile-details', kwargs={'pk': self.object.user.id})


class ProfileDeleteView(DeleteView, LoginRequiredMixin):
    model = UserModel
    template_name = 'accounts/profile-delete.html'
    form_class = ProfileDeleteForm
    success_url = reverse_lazy('home')
    success_message = 'Deleted Successfully'

    def get_context_data(self, **kwargs):
        context = super(ProfileDeleteView, self).get_context_data()
        profile = Profile.objects.get(pk=self.request.user.id)
        context['profile'] = profile
        return context


def build_404_view(request, exception):
    return render(request, '404.html')