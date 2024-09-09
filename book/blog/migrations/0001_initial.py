# Generated by Django 5.1 on 2024-09-09 09:01

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
                'verbose_name': 'Автор',
                'verbose_name_plural': 'Авторы',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='Текст')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
            ],
            options={
                'ordering': ['-time_create'],
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
                'verbose_name': 'Жанр',
                'verbose_name_plural': 'Жанры',
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
                ('photo_preview', models.ImageField(blank=True, upload_to='photos/photo_preview', verbose_name='Фото_превью')),
                ('photo_post', models.ImageField(blank=True, upload_to='photos/photo_post', verbose_name='Фото_статьи')),
                ('photo_header', models.ImageField(blank=True, upload_to='photos/photo_header', verbose_name='Фото_фон')),
                ('views', models.IntegerField(default=0, verbose_name='Кол-во просмотров')),
                ('year', models.IntegerField(default=0, verbose_name='Год')),
                ('number_series', models.IntegerField(default=1, verbose_name='Номер книги серии')),
                ('file_book', models.FileField(blank=True, upload_to='books', verbose_name='скачать')),
                ('is_published', models.BooleanField(default=True, verbose_name='Статус')),
            ],
            options={
                'verbose_name': 'Статью',
                'verbose_name_plural': 'Статьи',
                'ordering': ['-time_create'],
            },
        ),
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=255, verbose_name='Серия')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='url')),
            ],
            options={
                'verbose_name': 'Серия (Цикл)',
                'verbose_name_plural': 'Серии (Цикл)',
                'ordering': ['title'],
            },
        ),
    ]
