from django.contrib import admin
from .models import AddBook


@admin.register(AddBook)  # app registration
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'mail', 'created_at', 'is_published')
