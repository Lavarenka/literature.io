from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    we add avatars to the standard model (get_user_model)
    """
    image = models.ImageField(upload_to="users/images/", blank=True, null=True, verbose_name="Фото профиля")

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
