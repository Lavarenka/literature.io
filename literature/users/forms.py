from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm


class LoginUserForm(AuthenticationForm):
    """
    авторизация
    """
    username = forms.CharField(label="Логин/Email",
                               widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label="Пароль",
                               widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        """
        get_user_model стандартная модель пользователя
        """
        model = get_user_model()
        fields = ['username', 'password']


class RegisterUserForm(UserCreationForm):
    """
    регистрация пользователя

    уникальность паролей проверяет  UserCreationForm
    """
    username = forms.CharField(label="Логин", widget=forms.TextInput(attrs={'class': 'form-input'}))

    password1 = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
        labels = {
            'email': 'E-mail',
            'first_name': 'Имя',
            'last_name': 'Фамилия',
        }

        # widgets = {
        #     'email': forms.TextInput(attrs={'class': 'form-input'}),
        #     'first_name': forms.TextInput(attrs={'class': 'form-input'}),
        #      'last_name': forms.TextInput(attrs={'class': 'form-input'}),
        # }

    def clean_email(self):
        """проверка на уникальность email"""
        email = self.cleaned_data['email']
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError("Такой email уже существует")
        return email


class ProfileUserForm(forms.ModelForm):
    """
    Профиль пользователя
    disabled=True // нельзя редактировать
    """
    username = forms.CharField(disabled=True, label="Логин",
                               widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.CharField(disabled=True, label="E-mail",
                            widget=forms.TextInput(attrs={'class': 'form-input'}))

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'first_name', 'last_name', ]
        labels = {
            'first_name': 'Имя',
            'last_name': 'Фамилия',
        }

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-input'}),
            'last_name': forms.TextInput(attrs={'class': 'form-input'}),
        }


class UserPasswordChangeForm(PasswordChangeForm):
    """
    смена пароля
    """
    old_password = forms.CharField(label='Старый пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    new_password1 = forms.CharField(label='Новый пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    new_password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
