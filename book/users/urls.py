from django.urls import path
from django.contrib.auth.views import LogoutView, PasswordChangeView, PasswordChangeDoneView, PasswordResetView, \
    PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from .views import *

# app_name = "users"

urlpatterns = [
    path('register/', RegisterUser.as_view(), name='register'),  # регистрация
    path('login/', LoginUser.as_view(), name='login'),  # authorization
    path('logout/', logout_user, name='logout'),  # выход
    path('profile/', ProfileUser.as_view(), name='profile'),
    path('password-change/', UserPasswordChange.as_view(), name='password-change'), # смена пароля
    # path('favorites/<int:id>/', UserFavoritesView.as_view(), name='favorites'),
    # path('add_to_favorite/<int:id>', add_to_favorite, name="add_to_favorite"),
    # path('remove_from_favorite/<int:id>', remove_from_favorite, name="remove_from_favorite"),
    # path('suggest_article/', UserArticle.as_view(), name="suggest_article"),

    path('password-reset/',
         PasswordResetView.as_view(template_name='users/password_reset_form.html',
                                   email_template_name='users/password_reset_email.html',
                                   success_url=reverse_lazy('password_reset_done')
                                   ),
         name='password_reset'),  # форма емаил
    path('password-reset/done/', PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
         name='password_reset_done'),  # инструкция

    path('password-reset/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html',
                                          success_url=reverse_lazy('password_reset_complete')),
         name='password_reset_confirm'),  # одноразова ссылка
    path('password-reset/complete/',
         PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
         name='password_reset_complete'),  # форма успешной смены пароля
]
