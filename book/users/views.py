from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import CreateView, ListView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import *
from django.contrib.auth import authenticate, login
from django.contrib import messages
from blog.models import Post


class RegisterUser(SuccessMessageMixin, CreateView):
    """

    """
    form_class = RegisterUserForm
    template_name = "users/register.html"
    extra_context = {"title": "Регистрация"}
    success_url = reverse_lazy('login')
    success_message = "Вы успешно зарегистрировались! Для входа в систему ,авторизуйтесь."


class LoginUser(SuccessMessageMixin, LoginView):
    """
    авторизация
    """
    form_class = LoginUserForm
    template_name = 'users/login.html'
    extra_context = {'title': 'Авторизация'}
    success_message = "Вы успешно авторизованы! "

    def get_success_url(self):
        # перенапровление
        return reverse_lazy('home')

class ProfileUser(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    """
    Profile user

    """
    model = User
    form_class = ProfileUserForm
    template_name = 'users/profile.html'
    extra_context = {'title': 'Профиль пользователя'}
    success_message = "Профиль изменен "


    def get_success_url(self):
        """
        redirect to profile
        """
        return reverse_lazy('profile')

    def get_object(self, queryset=None):
        """
        in the profile takes the logged in user
        """
        return self.request.user

class UserPasswordChange(SuccessMessageMixin, PasswordChangeView):
    """
    смена пароля
    """
    form_class = UserPasswordChangeForm
    success_url = reverse_lazy("profile")
    template_name = "users/password-change-form.html"
    extra_context = {'title': 'Изменение пароля'}
    success_message = "Пароль изменен "



def logout_user(request):
    """
    if you logged out of your account and were on the user’s page,
    it redirects to the main page
    """
    logout(request)
    try:
        return HttpResponseRedirect(reverse('home'))
    except:
        return HttpResponseRedirect(request.META.get("HTTP_REFERER", "/"))