from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django import forms

from users.models import User


class DateInput(forms.DateInput):
    input_type = 'date'


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'birthday', 'sex', 'username', 'email', 'password1', 'password2')
        widget = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите имя'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите фамилию'}),
            'birthday': forms.SelectDateWidget(attrs={'class': 'form-control', 'placeholder': 'Введите день рождения'}),
            'sex': forms.RadioSelect(attrs={'class': 'form-control', 'placeholder': 'Выберите пол'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите логин'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Введите email'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Введите пароль'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Введите пароль'}),
        }


class UserProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'birthday', 'sex', 'username', 'email')
        widget = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'birthday': DateInput(attrs={'class': 'form-control'}),
            'sex': forms.RadioSelect(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'readonly': True}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'readonly': True}),
        }
