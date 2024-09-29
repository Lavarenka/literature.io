from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Genre, Comment, Series, Author, Post

"""
Admin panel settings:
    list_display // display fields in articles
    list_display_links // clickability of fields
    ordering // sorting records for admin
    list_editable // the ability to edit without entering the article
    EDITABLE FIELD CANNOT BE CLICKABLE
    list_per_page // pagination, displaying articles on the admin panel
    search_fields // search in the database
    list_filter // filter
"""


@admin.register(Genre)  # reg app
class GenreAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}  # to automatically add a slug


@admin.register(Comment)  # reg app
class PostComment(admin.ModelAdmin):
    list_display = ('author', 'com',)


@admin.register(Series)  # reg app
class SeriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}  # to automatically add a slug


@admin.register(Author)  # reg app
class AuthorAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}  # to automatically add a slug


@admin.register(Post)  # reg app
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'number_series', 'series', 'author', 'is_published', 'photo_preview', 'origin')
    prepopulated_fields = {"slug": ("title",)}  # to automatically add a slug
    list_editable = ('is_published',)
    readonly_fields = ['views', ]
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    list_filter = ('is_published',)

    save_on_top = True  # save buttons at the top and bottom

    @admin.display(description='Фото_превью', ordering='content')
    def post_photo(self, obj):
        """ display photos in articles """
        if obj.photo_preview:
            return mark_safe(f"<img src='{obj.photo_preview.url}' width=50")
        return 'без фото '
