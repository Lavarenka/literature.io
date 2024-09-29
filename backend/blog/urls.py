from django.urls import path
from .views import Home, GetPost, PostGenre, PostSeries, PostFilter, CommentBook, PostAuthor, DelComment, Search

urlpatterns = [
    path('comment/<int:pk>/', CommentBook.as_view(), name='create_comment'),
    # sending a comment, must be the first in the urls

    path('', Home.as_view(), name='home'),
    path('post/<str:slug>/', GetPost.as_view(), name='post'),
    path('genre/<str:slug>/', PostGenre.as_view(), name='genre'),
    path('series/<str:slug>/', PostSeries.as_view(), name='series'),
    path('author/<str:slug>/', PostAuthor.as_view(), name='author'),
    path('sorted/', PostFilter.as_view(), name='sorted'),
    path('delete_comment/<int:pk>', DelComment.as_view(), name='delete_comment'),
    path('search/', Search.as_view(), name='search'),

]
