from django.contrib.auth import get_user_model
from django.db import models

from users.models import User

"""
AddBook

title, content, is_completed, email, created_at

"""

class AddBook(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    content = models.TextField()
    is_published = models.BooleanField(default=False)
    mail = models.EmailField(max_length=254, verbose_name='Email' )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')

    def __str__(self):
        return self.title

