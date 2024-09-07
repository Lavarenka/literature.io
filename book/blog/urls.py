from django.urls import path
from .views import Home, GetPost, PostGenre, PostSeries, PostFilter

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('post/<str:slug>/', GetPost.as_view(), name='post'),  # вывод отдельного поста
    path('genre/<str:slug>/', PostGenre.as_view(), name='genre'),  # жанры
    path('series/<str:slug>/', PostSeries.as_view(), name='series'),  # серии книг
    path('sorted/', PostFilter.as_view(), name='sorted'),  # серии книг
]
