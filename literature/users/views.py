from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from .forms import LoginUserForm, RegisterUserForm
from .models import *
from django.db.models import F
from django.contrib import messages


def register_user(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, 'Вы успешно зарегистрировались, для входа в систему необходио авторизоватся')
            # return render(request, 'users/register.html')
            return redirect('users:login')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = RegisterUserForm()
    return render(request, 'users/register.html', {"form": form, "title": "Регистрация"})



# def login_user(request):
#     if request.method == 'POST':
#         form = LoginUserForm(request.POST)  # импорт формы
#         if form.is_valid():
#             cd = form.cleaned_data
#             user = authenticate(request, username=cd['username'],
#                                 password=cd['password'])  # username, password - из формы
#             if user and user.is_active:
#                 login(request, user)
#                 messages.success(request, 'Вы вошли')
#                 return HttpResponseRedirect(reverse('home'))
#             else:
#                 messages.error(request, 'Нет такого пользователя')
#         else:
#             messages.error(request, 'Ошибка авторизации')
#     else:
#
#         form = LoginUserForm()  # импорт формы
#     return render(request, 'users/login.html', {"form": form, "title": "Авторизация"})

class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'users/login.html'
    extra_context = {'title': 'Авторизация'}

    def get_success_url(self):
        # перенапровление
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('users:login'))