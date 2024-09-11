from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models
from blog.models import Post


class User(AbstractUser):
    image = models.ImageField(upload_to="users/images/", blank=True, null=True, verbose_name="Фото профиля")

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"




