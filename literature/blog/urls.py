from django.urls import path
from .views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('genre/<str:slug>/', get_genre, name='genre'),
    path('post/<str:slug>/', get_post, name='post'),
]
