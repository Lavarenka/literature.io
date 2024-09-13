from django.contrib import admin
from .models import SocialItem


@admin.register(SocialItem)
class SocialItemAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("id", "name")
    search_fields = ("name",)
