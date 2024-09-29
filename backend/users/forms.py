from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from users.models import User


class RegisterUserForm(UserCreationForm):
    """
    user registration
    UserCreationForm checks password uniqueness
    """
    username = forms.CharField(label="Логин", widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="Email", widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'image', 'password1', 'password2']
        labels = {
            'email': 'E-mail',
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'image': 'Аватар',
        }

    def clean_email(self):
        """ email uniqueness check """
        email = self.cleaned_data['email']
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError("Такой email уже существует")
        return email


class LoginUserForm(AuthenticationForm):
    """
    authorization
    """
    username = forms.CharField(label="Логин/Email",
                               widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label="Пароль",
                               widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ['username', 'password']


class ProfileUserForm(forms.ModelForm):
    """
    User profile
    disabled=True // can't be edited
    """
    username = forms.CharField(disabled=True, label="Логин",
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(disabled=True, label="E-mail",
                            widget=forms.TextInput(attrs={'class': 'form-control'}))

    # image = forms.ImageField(required=False, widget=forms.FileInput(attrs={'class': 'fadeIn second',
    #                                                                        'placeholder': 'аватар', }))

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'image', ]
        labels = {
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'image': 'Аватар',
        }

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
        }


class UserPasswordChangeForm(PasswordChangeForm):
    """
    change password
    """
    old_password = forms.CharField(label='Старый пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password1 = forms.CharField(label='Новый пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password2 = forms.CharField(label='Подтверждение пароля',
                                    widget=forms.PasswordInput(attrs={'class': 'form-control'}))
