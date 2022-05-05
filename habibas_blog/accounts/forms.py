from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

UserModel = get_user_model()


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('email',)


class UserChangeAdminForm(UserChangeForm):
    class Meta:
        model = UserModel
        fields =('email',)
