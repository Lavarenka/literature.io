# Generated by Django 5.0.2 on 2024-05-31 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_file_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='file_book',
            field=models.FileField(blank=True, upload_to='books', verbose_name='скачать'),
        ),
        migrations.AlterField(
            model_name='post',
            name='photo_header',
            field=models.ImageField(blank=True, upload_to='photos_header', verbose_name='Фото_фон'),
        ),
    ]
