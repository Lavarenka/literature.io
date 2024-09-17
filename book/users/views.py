from django.contrib.auth import logout
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import RegisterUserForm, LoginUserForm, ProfileUserForm, UserPasswordChangeForm
from .models import User


class RegisterUser(SuccessMessageMixin, CreateView):
    """
    user registration
    """
    form_class = RegisterUserForm
    template_name = "users/register.html"
    extra_context = {"title": "Регистрация"}
    success_url = reverse_lazy('login')
    success_message = "Вы успешно зарегистрировались! Для входа в систему ,авторизуйтесь."




class LoginUser(SuccessMessageMixin, LoginView):
    """
    user authorization
    """
    form_class = LoginUserForm
    template_name = 'users/login.html'
    extra_context = {'title': 'Авторизация'}
    success_message = "Вы успешно авторизованы! "

    # def get_success_url(self):
    #     # redirection
    #     return reverse_lazy('home')

class ProfileUser(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    """
    user profile
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
    change password
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

    return HttpResponseRedirect(request.META.get("HTTP_REFERER", "/"))