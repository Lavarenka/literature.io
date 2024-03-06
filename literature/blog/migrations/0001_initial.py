# Generated by Django 5.0.2 on 2024-03-06 15:59

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='url')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='url')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='url')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='url')),
                ('content', models.TextField(blank=True)),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='Время изменения')),
                ('photo_preview', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d', verbose_name='Фото_превтю')),
                ('photo_post', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d', verbose_name='Фото_статьи')),
                ('photo_header', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d', verbose_name='Фото_фон')),
                ('views', models.IntegerField(default=0, verbose_name='Кол-во просмотров')),
                ('year', models.IntegerField(default=0, verbose_name='Год')),
                ('number_series', models.IntegerField(default=1, verbose_name='Номер книги серии')),
                ('score', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)])),
                ('is_published', models.BooleanField(choices=[(False, 'Черновик'), (True, 'Опубликовано')], default=1, verbose_name='Статус')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='authors', to='blog.author', verbose_name='Автор')),
                ('genre', models.ManyToManyField(related_name='posts', to='blog.genre', verbose_name='Жанры')),
                ('series', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='posts', to='blog.series', verbose_name='Серии книг')),
            ],
            options={
                'ordering': ['-time_create'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя пользователя')),
                ('content', models.TextField(verbose_name='Текст')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('com', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='blog.post')),
            ],
        ),
    ]
