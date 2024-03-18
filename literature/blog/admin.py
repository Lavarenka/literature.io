from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *

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


@admin.register(Genre)  # регистрация приложения
class GenreAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}  # для автоматического добавления слага


@admin.register(Series)  # регистрация приложения
class SeriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}  # для автоматического добавления слага


@admin.register(Author)  # регистрация приложения
class AuthorAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}  # для автоматического добавления слага


@admin.register(Post)  # регистрация приложения
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'number_series', 'series', 'author', 'is_published', 'post_photo')
    prepopulated_fields = {"slug": ("title",)}  # для автоматического добавления слага
    list_editable = ('is_published', )
    readonly_fields = ['views', 'score']
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

@admin.register(Comment)  # регистрация приложения
class PostComment(admin.ModelAdmin):
    pass
