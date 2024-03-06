from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

# Create your models here.

"""
жанр: genre (Many to Many)
title , slug

серия: series (ForeignKey)
title , slug

Автор: author (ForeignKey)
title , slug

comment: (ForeignKey)
/

Post:
title , slug, content, created_at, edit_at, photo_preview, photo_post, photo_header, 
genre, series, number_series, author, year, views, comment, rating

"""


class Genre(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, verbose_name='url', unique=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']



class Series(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, verbose_name='url', unique=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']


class Author(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, verbose_name='url', unique=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']

class Post(models.Model):
    """


    """

    class Status(models.IntegerChoices):
        # для публикаций
        DRAFT = 0, 'Черновик'
        PUBLICHED = 1, 'Опубликовано'

    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, verbose_name='url', unique=True, )
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    photo_preview = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, verbose_name='Фото_превтю')
    photo_post = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, verbose_name='Фото_статьи')
    photo_header = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, verbose_name='Фото_фон')
    views = models.IntegerField(default=0, verbose_name='Кол-во просмотров')
    year = models.IntegerField(default=0, verbose_name='Год')
    number_series = models.IntegerField(default=1, verbose_name='Номер книги серии')
    score = models.IntegerField(default=0, validators=[
        MaxValueValidator(5),
        MinValueValidator(0),
    ])
    genre = models.ManyToManyField(Genre, related_name='posts',
                                   verbose_name='Жанры')
    series = models.ForeignKey(Series, on_delete=models.PROTECT, related_name='posts',
                               verbose_name='Серии книг')  # связываем категории, PROTECT запрещает удаление если есть посты
    author = models.ForeignKey(Author, on_delete=models.PROTECT, related_name='authors',
                               verbose_name='Автор')
    is_published = models.BooleanField(choices=tuple(map(lambda x: (bool(x[0]), x[1]), Status.choices)),
                                       default=Status.PUBLICHED, verbose_name='Статус')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-time_create']


class Comment(models.Model):
    """создаем коменты и подключаем к посту
        нужно еще добавить дату
    """

    name = models.CharField(max_length=100, verbose_name='Имя пользователя')
    content = models.TextField(verbose_name='Текст')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    com = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment')
