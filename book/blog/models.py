from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class Genre(models.Model):
    """ genres, connect to the ManyToMany post """
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, verbose_name='url', unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """
        method for calling a post link by slug
        genre - route in url
        """
        return reverse('genre', kwargs={"slug": self.slug})

    class Meta:
        ordering = ['title']
        verbose_name = 'Жанр'  # admin panel header
        verbose_name_plural = 'Жанры'  # admin panel title in plural


class Series(models.Model):
    """ series, connect to the ForeignKey post """
    title = models.CharField(max_length=255, db_index=True, verbose_name='Серия')
    slug = models.SlugField(max_length=255, verbose_name='url', unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """
        method for calling a post link by slug
        series - route in url
        """
        return reverse('series', kwargs={"slug": self.slug})

    class Meta:
        ordering = ['title']
        verbose_name = 'Серия (Цикл)'  # admin panel header
        verbose_name_plural = 'Серии (Цикл)'  # admin panel title in plural


class Author(models.Model):
    """ author, connect to the ForeignKey post """
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, verbose_name='url', unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """
        method for calling a post link by slug
        author - route in url
        """
        return reverse('author', kwargs={"slug": self.slug})

    class Meta:
        ordering = ['title']
        verbose_name = 'Автор'  # admin panel header
        verbose_name_plural = 'Авторы'  # admin panel title in plural


class Post(models.Model):
    """

    auto_now_add / filled in automatically only after creating a post
    auto_now / filled automatically after each save
    """

    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, verbose_name='url', unique=True, )
    content = models.TextField(blank=True, verbose_name='Описание')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    photo_preview = models.ImageField(upload_to='photos/photo_preview', blank=True, verbose_name='Фото_превью')
    photo_post = models.ImageField(upload_to='photos/photo_post', blank=True, verbose_name='Фото_статьи')
    photo_header = models.ImageField(upload_to='photos/photo_header', blank=True, verbose_name='Фото_фон')
    views = models.IntegerField(default=0, verbose_name='Кол-во просмотров')
    year = models.IntegerField(default=0, verbose_name='Год')
    number_series = models.IntegerField(default=1, verbose_name='Номер книги серии')
    file_book = models.FileField(upload_to='books', verbose_name='скачать', blank=True)

    genre = models.ManyToManyField(Genre, related_name='genre',
                                   verbose_name='Жанры')
    series = models.ForeignKey(Series, on_delete=models.SET_NULL, null=True, related_name='post',
                               verbose_name='Серии книг',
                               blank=True)  # link categories, PROTECT prohibits deletion if there are posts
    author = models.ForeignKey(Author, on_delete=models.PROTECT, related_name='author',
                               verbose_name='Автор')
    is_published = models.BooleanField(default=True, verbose_name='Статус')
    origin = models.TextField(blank=True, verbose_name='Источник')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """
        method for calling a post link by slug
        post - route in url
        """
        return reverse('post', kwargs={"slug": self.slug})

    class Meta:
        """
        for admin
        """
        ordering = ['-time_create']  # It is mapped both in the admin panel and on the website
        verbose_name = 'Книгу'  # admin panel header
        verbose_name_plural = 'Книги'  # admin panel title in plural


class Comment(models.Model):
    """ create comments and connect to the post """
    content = models.TextField(verbose_name='Текст')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    com = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment')
    author = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, related_name='posts', null=True,
                               default=None)

    class Meta:
        ordering = ['-time_create']
        verbose_name = 'Комментарий'  # admin panel header
        verbose_name_plural = 'Комментарии'  # admin panel title in plural
