from django import forms
from .models import *

"""
"""


class CommentForm(forms.ModelForm):
    """

    """

    class Meta:
        model = Comment
        fields = ['name', 'content', ]  # все поля с модели
