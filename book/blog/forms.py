from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    """

    """

    class Meta:
        model = Comment
        fields = ['content', ]  # все поля с модели
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }