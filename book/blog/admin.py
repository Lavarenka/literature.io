from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Genre, Comment, Series, Author, Post

"""
настройка даминки статьи
    list_display // отображение полей в статьи
    list_display_links // кликабельность полей
    ordering // сортировка записей для админки
    list_editable // возможность редоктирования не входя в статью
    РЕДАКТИРУЕМОЕ ПОЛЕ НЕ МОЖЕТ БЫТЬ КЛИКАБЕЛЬНЫМ
    list_per_page // пагинация, отображение статей на админку
    search_fields // поиск в базе 
    list_filter // фильтр
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
    list_display = ('id', 'title', 'number_series', 'series', 'author', 'is_published', 'photo_preview')
    prepopulated_fields = {"slug": ("title",)}  # to automatically add a slug
    list_editable = ('is_published', )
    readonly_fields = ['views', ]
    list_display_links = ('id', 'title')
    search_fields = ('title', )
    list_filter = ('is_published', )

    save_on_top = True  # кнопки сохранить сверху и снизу

    @admin.display(description='Фото_превью', ordering='content')
    def post_photo(self, obj):
        """отображение фото в статьях"""
        if obj.photo_preview:
            return mark_safe(f"<img src='{obj.photo_preview.url}' width=50")
        return 'без фото '