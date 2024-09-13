from django.urls import path
from .views import add_book

urlpatterns = [
    path('add_books/', add_book, name='add_book'),
]