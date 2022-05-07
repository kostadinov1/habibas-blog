from django import forms

from habibas_blog.core.models import Comment


class CommentForm(forms.ModelForm):



    class Meta:
        model = Comment
        fields = ('content',)
        widgets={
            'content': forms.TextInput(
                attrs={
                    'rows': 6
                }
            )
        }