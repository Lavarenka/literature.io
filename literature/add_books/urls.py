from django.urls import path
from .views import *

urlpatterns = [
    path('', AddBook.as_view(), name='add_book'),


]
