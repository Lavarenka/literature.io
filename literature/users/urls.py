from django.contrib.auth.views import LogoutView, PasswordChangeView, PasswordChangeDoneView, PasswordResetView, \
    PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import path
from .views import *
from django.urls import reverse, reverse_lazy

app_name = "users"

urlpatterns = [
    path('register/', RegisterUser.as_view(), name='register'),  # регистрация
    path('login/', LoginUser.as_view(), name='login'),  # авторизация
    path('password-change/', UserPasswordChange.as_view(), name='password-change'),  # смена пароля

    path('password-reset/',
         PasswordResetView.as_view(template_name='users/password_reset_form.html',
                                   email_template_name='users/password_reset_email.html',
                                   success_url=reverse_lazy('users:password_reset_done')
                                   ),
         name='password_reset'),  # форма емаил
    path('password-reset/done/', PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
         name='password_reset_done'),  # инструкция

    path('password-reset/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html',
                                          success_url=reverse_lazy('users:password_reset_complete')),
         name='password_reset_confirm'),  # одноразова ссылка
    path('password-reset/complete/',
         PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
         name='password_reset_complete'),  # форма успешной смены пароля

    path('logout/', logout_user, name='logout'),  # выход
    path('profile/', ProfileUser.as_view(), name='profile'),  # профиль

]
