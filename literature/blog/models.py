from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.urls import reverse

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



db_index=True // индексирует поле , более быстрое для поиска 
null=True // проставляет пустые поля , для связей
"""


class PublishedManager(models.Manager):
    """
    возвращает все опубликованные статьи
    """

    def get_queryset(self):
        return super().get_queryset().filter(is_published=Post.Status.PUBLICHED)


class Genre(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, verbose_name='url', unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('genre', kwargs={"slug": self.slug})

    class Meta:
        ordering = ['title']
        verbose_name = 'Жанр'  # название блога в админке
        verbose_name_plural = 'Жанры'  # название блога в админке во множественном числе


class Series(models.Model):
    title = models.CharField(max_length=255, db_index=True, verbose_name='Серия')
    slug = models.SlugField(max_length=255, verbose_name='url', unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # метод для вызова ссылки на пост по слагу
        # series - маршрут в урлах
        return reverse('series', kwargs={"slug": self.slug})

    class Meta:
        ordering = ['title']
        verbose_name = 'Серия (Цикл)'  # название блога в админке
        verbose_name_plural = 'Серии (Цикл)'  # название блога в админке во множественном числе


class Author(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, verbose_name='url', unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # метод для вызова ссылки на пост по слагу
        # series - маршрут в урлах
        return reverse('author', kwargs={"slug": self.slug})

    class Meta:
        ordering = ['title']
        verbose_name = 'Автор'  # название блога в админке
        verbose_name_plural = 'Авторы'  # название блога в админке во множественном числе




class Post(models.Model):
    """
    auto_now_add / заполняется автоматом только после создания
    auto_now / заполняется автоматом после каждого сохранения
    посмотреть filefild
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
    photo_header = models.ImageField(upload_to='photos_header', blank=True, verbose_name='Фото_фон')
    views = models.IntegerField(default=0, verbose_name='Кол-во просмотров')
    year = models.IntegerField(default=0, verbose_name='Год')
    number_series = models.IntegerField(default=1, verbose_name='Номер книги серии')
    file_book = models.FileField(upload_to='books', verbose_name='скачать', blank=True)

    genre = models.ManyToManyField(Genre, related_name='genre',
                                   verbose_name='Жанры')
    series = models.ForeignKey(Series, on_delete=models.SET_NULL, null=True, related_name='post',
                               verbose_name='Серии книг',
                               blank=True)  # связываем категории, PROTECT запрещает удаление если есть посты
    author = models.ForeignKey(Author, on_delete=models.PROTECT, related_name='author',
                               verbose_name='Автор')

    is_published = models.BooleanField(choices=tuple(map(lambda x: (bool(x[0]), x[1]), Status.choices)),
                                       default=Status.PUBLICHED, verbose_name='Статус')

    objects = models.Manager()
    published = PublishedManager()  # вызываем класс со статьями опубликованными  , класс прописан Выше

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # метод для вызова ссылки на пост по слагу
        # post - маршрут в урлах
        return reverse('post', kwargs={"slug": self.slug})

    class Meta:
        """
        для адмнки
        """
        ordering = ['-time_create']  # сартирует и в админке и на сайте
        verbose_name = 'Статья'  # название блога в админке
        verbose_name_plural = 'Статьи'  # название блога в админке во множественном числе


class Comment(models.Model):
    """создаем коменты и подключаем к посту
        нужно еще добавить дату
        get_user_model() / функция для получения модели пользователя
    """

    # name = models.CharField(max_length=100, verbose_name='Имя пользователя', blank=True, null=True)

    content = models.TextField(verbose_name='Текст')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    com = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment')
    author = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, related_name='posts', null=True,
                               default=None)

    # def __str__(self):
    #     return self.id
    class Meta:
        """
        для адмнки
        """
        ordering = ['-time_create']  # сартирует и в админке и на сайте



class RatingStar(models.Model):
    """
    для звезд рейтинга к книге
    """
    value = models.SmallIntegerField('Значение', default=0)

    def __str__(self):
        return f'{self.value}'

    class Meta:
        verbose_name: 'Звезда рейтинга'
        verbose_name_plural = 'Звезды рейтинга'
        ordering = ["-value"]

class Rating(models.Model):
    """
    рейтинг , связываем с книгами и звездами
    """
    ip = models.CharField('IP адрес', max_length=15)
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE, verbose_name='звезда')
    post = models.ForeignKey(Post, on_delete=models.SET_NULL, verbose_name='книга', null=True,
                               default=None, blank=True, related_name="rating")

    def __str__(self):
        return f"{self.star} - {self.post}"

    class Meta:
        verbose_name = "Рейтинг"
        verbose_name_plural = "Рейтинги"