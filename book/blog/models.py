from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.urls import reverse


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

    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, verbose_name='url', unique=True, )
    content = models.TextField(blank=True)
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
    series = models.ForeignKey(Series, on_delete=models.SET_NULL, null=True, related_name='series',
                               verbose_name='Серии книг',
                               blank=True)  # связываем категории, PROTECT запрещает удаление если есть посты
    author = models.ForeignKey(Author, on_delete=models.PROTECT, related_name='author',
                               verbose_name='Автор')
    is_published = models.BooleanField(default=True, verbose_name='Статус')

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
        verbose_name = 'Статью'  # название блога в админке
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

    class Meta:
        ordering = ['-time_create']
        verbose_name = 'Комментарий'  # название блога в админке
        verbose_name_plural = 'Комментарии'  # название блога в админке во множественном числе

    class Meta:
        """
        для адмнки
        """
        ordering = ['-time_create']  # сартирует и в админке и на сайте
