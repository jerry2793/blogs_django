from django import forms

from django.contrib.auth.models import User
from .models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = 'user','profile_pic','signiture','theme'

class LoginForm(forms.Form):
    username = forms.CharField(label="Username")
    password = forms.PasswordInput()
    password2 = forms.PasswordInput()
    # class Meta:
    #     model = User
    #     fields = 'username','password'
        

class RegisterForm(forms.Form):
    username = forms.CharField()
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)

    email = forms.EmailInput()

    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())



class UpdatePwdForm(forms.ModelForm):
    username = forms.CharField(max_length=500,label="Username")
    password = forms.PasswordInput()
    password2 = forms.PasswordInput()
    class Meta:
        # password = 
        model = User
        fields = 'username','password'
        widgets = {
            'password':forms.PasswordInput()
        }