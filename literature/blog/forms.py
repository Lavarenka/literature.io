from django import forms
from .models import *

"""
"""


class CommentForm(forms.ModelForm):
    """

    """

    class Meta:
        model = Comment
        fields = ['content', ]  # все поля с модели


class RatingForm(forms.ModelForm):
    """
    Форма добавления рейтинга
    """
    star = forms.ModelChoiceField(queryset=RatingStar.objects.all(), widget=forms.RadioSelect(), empty_label=None)

    class Meta:
        model = Rating
        fields = ("star", )
