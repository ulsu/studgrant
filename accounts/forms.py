# -*- coding: utf-8 -*-
from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'autofocus': '', 'size': 60, 'placeholder': 'E-mail'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'size': 60, 'placeholder': 'Пароль'}))
    remember_me = forms.BooleanField(label='Запомнить меня', required=False)


