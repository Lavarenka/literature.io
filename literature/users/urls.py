from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import *

app_name = "users"

urlpatterns = [
    path('register/', register_user, name='register'),  # регистрация
    path('login/', LoginUser.as_view(), name='login'),  # авторизация
    path('logout/', logout_user, name='logout'),  # выход
]
