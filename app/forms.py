from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SignUp(UserCreationForm):
    username = forms.CharField(label='',
                               max_length=30,
                               widget=forms.TextInput(
                                   attrs={'class': 'control-form', 'placeholder': 'نام کاربری دلخواه خود را وارد کنید'}
                               ))
    password1 = forms.CharField(label='',
                                max_length=8,
                                widget=forms.PasswordInput(
                                    attrs={'class': 'control-form', 'placeholder': 'رمز عبور خود را وارد کنید'}
                                ))

    password2 = forms.CharField(label='',
                                max_length=8,
                                widget=forms.PasswordInput(
                                    attrs={'class': 'control-form', 'placeholder': 'رمز خود  را دوباره وارد کنید'}
                                ))


class Meta:
    model = User
    fields = ('username', 'password1', 'password2')
