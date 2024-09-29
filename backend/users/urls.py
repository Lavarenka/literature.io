from django.urls import path, reverse_lazy
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, \
    PasswordResetCompleteView
from .views import RegisterUser, LoginUser, logout_user, ProfileUser, UserPasswordChange

urlpatterns = [
    path('register/', RegisterUser.as_view(), name='register'),  # registration
    path('login/', LoginUser.as_view(), name='login'),  # authorization
    path('logout/', logout_user, name='logout'),  # exit
    path('profile/', ProfileUser.as_view(), name='profile'),  # profile
    path('password-change/', UserPasswordChange.as_view(), name='password-change'),  # change password

    path('password-reset/',
         PasswordResetView.as_view(template_name='users/password_reset_form.html',
                                   email_template_name='users/password_reset_email.html',
                                   success_url=reverse_lazy('password_reset_done')
                                   ),
         name='password_reset'),  # email form
    path('password-reset/done/', PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
         name='password_reset_done'),  # instruction

    path('password-reset/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html',
                                          success_url=reverse_lazy('password_reset_complete')),
         name='password_reset_confirm'),  # one-time link
    path('password-reset/complete/',
         PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
         name='password_reset_complete'),  # successful password change form
]
