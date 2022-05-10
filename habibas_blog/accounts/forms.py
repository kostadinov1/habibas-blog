from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from habibas_blog.accounts.models import Profile
from habibas_blog.common.mixins import DisabledFieldsFormMixin

UserModel = get_user_model()


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('email',)


class UserChangeAdminForm(UserChangeForm):
    class Meta:
        model = UserModel
        fields =('email',)



class ProfileCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Profile
        exclude=('user',)


class ProfileEditForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Profile
        exclude=('user',)


class ProfileDeleteForm(forms.ModelForm, DisabledFieldsFormMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_disabled_fields()

    class Meta:
        model = Profile
        exclude = ('user',)

