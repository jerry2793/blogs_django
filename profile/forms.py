from django import forms

from .models import Profile


class LoginForm(forms.ModelForm):
    username = forms.CharField(max_length=50)
    password = forms.PasswordInput()