from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import *
from .models import *
from django.db.models import F
from django.contrib import messages


class RegisterUser(SuccessMessageMixin, CreateView):
    """
    регистрация
    """
    form_class = RegisterUserForm
    template_name = 'users/register.html'
    extra_context = {"title": "Регистрация"}
    success_url = reverse_lazy('users:login')
    success_message = "Вы успешно зарегистрировались! "





# def register_user(request):
#     if request.method == 'POST':
#         form = RegisterUserForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.set_password(form.cleaned_data['password'])
#             user.save()
#             messages.success(request, 'Вы успешно зарегистрировались, для входа в систему необходио авторизоватся')
#             # return render(request, 'users/register.html')
#             return redirect('users:login')
#         else:
#             messages.error(request, 'Ошибка регистрации')
#     else:
#         form = RegisterUserForm()
#     return render(request, 'users/register.html', {"form": form, "title": "Регистрация"})


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
    Профиль пользователя
    """
    model = get_user_model()
    form_class = ProfileUserForm
    template_name = 'users/profile.html'
    extra_context = {'title': 'Профиль пользователя'}
    success_message = "Профиль изменен "

    def get_success_url(self):
        """
        перенапровление
        """
        return reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        """
        в профиле берет залогининого пользователя
        """
        return self.request.user


class UserPasswordChange(SuccessMessageMixin, PasswordChangeView):
    """
    смена пароля
    """
    form_class = UserPasswordChangeForm
    success_url = reverse_lazy("users:profile")
    template_name = "users/password-change-form.html"
    extra_context = {'title': 'Изменение пароля'}
    success_message = "Пароль изменен "


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('users:login'))
