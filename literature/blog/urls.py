from django.urls import path
from .views import *

urlpatterns = [
    path('comment/<int:pk>/', CommentBook.as_view(), name='create_comment'),
    # отправка комента , должно быть первым в урлах
    path('', Home.as_view(), name='home'),
    path('genre/<str:slug>/', PostGenre.as_view(), name='genre'),  # жанры
    path('series/<str:slug>/', PostSeries.as_view(), name='series'),  # серии книг
    path('author/<str:slug>/', PostAuthor.as_view(), name='author'),  # Автор
    path('post/<str:slug>/', GetPost.as_view(), name='post'),  # вывод отдельного поста
    path('search/', Search.as_view(), name='search'), # Поиск

]
