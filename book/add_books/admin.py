from django.contrib import admin
from .models import *



@admin.register(AddBook)  # регистрация приложения
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'mail', 'created_at', 'is_published')
