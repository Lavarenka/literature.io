from django.urls import path
from .views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('genre/<str:slug>/', PostGenre.as_view(), name='genre'), # жанры
    path('series/<str:slug>/', PostSeries.as_view(), name='series'), # серии книг
    path('post/<str:slug>/', GetPost.as_view(), name='post'),  # вывод отдельного поста
]
