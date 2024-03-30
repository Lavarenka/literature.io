from django import forms
from .models import *

"""
"""


class NewsForm(forms.ModelForm):
    """
    title, content, is_completed, email, created_at

    """
    class Meta:
        model = AddBook
        fields = ['title', 'content', 'mail',] # все поля с модели
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control',}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5,}),
            'mail': forms.EmailInput(attrs={'class': 'form-control',}),
        }


