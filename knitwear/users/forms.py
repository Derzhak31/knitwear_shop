from datetime import datetime
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django import forms

from users.models import User


SEX_CHOICES = (
    ('m', 'Мужской'),
    ('w', 'Женский'),
)
cur_year = datetime.today().year
YEARS_CHOICES = reversed(range(cur_year - 99, cur_year + 1))


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Введите логин'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control', 'placeholder': 'Введите пароль'
    }))

    class Meta:
        model = User
        fields = ('username', 'password')


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Введите имя'
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Введите фамилию'
    }))
    birthday = forms.DateField(
        widget=forms.SelectDateWidget(years=YEARS_CHOICES, attrs={
            'class': 'form-control', 'placeholder': 'Введите день рождения'
        }))
    sex = forms.CharField(widget=forms.Select(choices=SEX_CHOICES, attrs={
        'class': 'form-control', 'placeholder': 'Выберите пол'
    }))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Введите логин'
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control', 'placeholder': 'Введите email'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control', 'placeholder': 'Введите пароль'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control', 'placeholder': 'Введите пароль'
    }))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'birthday', 'sex', 'username', 'email', 'password1', 'password2')


class UserProfileForm(UserChangeForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    birthday = forms.CharField(widget=forms.SelectDateWidget(years=YEARS_CHOICES, attrs={'class': 'form-control'}))
    sex = forms.CharField(widget=forms.Select(choices=SEX_CHOICES, attrs={'class': 'form-control'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': True}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': True}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'birthday', 'sex', 'username', 'email')
