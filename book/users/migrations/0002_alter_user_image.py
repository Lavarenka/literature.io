# Generated by Django 5.1 on 2024-09-09 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, default='img/no-avatar.jpg', null=True, upload_to='users/images/', verbose_name='Фото профиля'),
        ),
    ]
