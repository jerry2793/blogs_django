from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
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
        

class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=100,label='Username')
    first_name = forms.CharField(max_length=50, label='First Name')
    last_name = forms.CharField(max_length=50, label='Last Name')

    email = forms.EmailField(label='Email')

    class Meta:
        model = User
        fields = ("username","first_name","last_name","email")

    



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