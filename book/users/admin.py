from django.contrib import admin
from .models import User
from django.contrib.auth.models import Group




@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "first_name", "last_name")
    list_filter = ("username",)

    save_on_top = True
    save_as = True

# @admin.register(Favorite)
# class FavoriteAdmin(admin.ModelAdmin):
#     list_display = ("id", "user")
#     list_filter = ("user",)
#
#     save_on_top = True
#     save_as = True
#
# @admin.register(SuggestArticle)
# class SuggestArticleAdmin(admin.ModelAdmin):
#     list_display = ("id", "author", "time_created", "is_processed",)
#     list_filter = ("author",)
#
#     save_on_top = True
#     save_as = True




