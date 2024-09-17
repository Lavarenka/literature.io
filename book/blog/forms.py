from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    """ Form for creating a comment """

    class Meta:
        model = Comment
        fields = ['content', ]  # all fields from the model
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }
