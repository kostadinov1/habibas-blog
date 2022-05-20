from django import forms
from habibas_blog.core.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
        widgets = {
            'content': forms.Textarea(
                attrs={
                    'rows': 3
                }
            )
        }


class ContactForm(forms.Form):
    name = forms.CharField(max_length=60, widget=forms.TextInput(attrs={'placeholder': 'Enter Your Name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Enter Your Email'}))
    message = forms.CharField(max_length=500, widget=forms.Textarea(attrs={'placeholder': 'Enter Message'}))
