from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views import View

from .models import Profile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm,
    UserChangeForm,
    PasswordChangeForm
)
from django.contrib.auth import (
    authenticate,
    update_session_auth_hash,
    login,
    logout,
)
from django.views.generic.edit import UpdateView

from .forms import *

# UserCreationForm = UserCreationForm

# Create your views here.
class LoginView(View):
    # def __init__(self):
    #     self.template = {
    #         'login':'login.html'
    #     }

    #     if self.request.method == "GET":
    #         self.request.POST = {}

    #     self.ctx = {
    #         'form':LoginForm(self.request.POST)
    #     }


    def get(self,*args,**kwargs):
        ctx = {
            'form':AuthenticationForm()
        }
        return render(self.request,'profile/login.html',ctx)
    
    def post(self,*args,**kwargs):
        user = self.request.POST
        user = authenticate(username=user['username'], password=user['password'])
        if user is not None:
            login(self.request,user)
            # next = self.request.POST.get('next', '/')
            return redirect('home')
        else:
            ctx = {
                'msg':'Cannot Find User from Backend',
                'form':AuthenticationForm(user)
            }
            return render(self.request,'profile/login.html',ctx)


class RegisterView(View):
    def get(self,*args,**kwargs):
        ctx = {
            'form':RegisterForm()
        }
        return render(self.request,'profile/register.html',ctx)

    def post(self,*args,**kwargs):
        ctx = {
            'msg':'',
            'form':RegisterForm(self.request.POST)
        }
        registerForm = ctx['form']
        if registerForm.is_valid():
            registerForm.save()
            return redirect('login')
        # if registerForm.is_valid():
        #     registerForm = registerForm.cleaned_data
        #     print(registerForm['password1'])
        #     print(registerForm['password2'])
        #     if registerForm['password1'] == registerForm['password2']:
        #     # print(registerForm)
        #         registerForm['password'] = str(registerForm['password1'])
        #         print(type(registerForm))
        #         print(registerForm)
        #         registerForm.pop("password1").pop("password2")
        #         User.objects.create(
        #             registerForm
        #         )
        #         return redirect("login")

            # else:
            #     ctx['msg'] = "passwords does not match"
            #     return render(self.request,'profile/register.html',ctx)
            
        else:
            ctx['msg'] = "Form is not valid"
            return render(self.request,'profile/register.html',ctx)


class SetProfileView(View):
    def get(self,*args,**kwargs):
        # try:
        #     userProfile = Profile.objects.filter(user=self.request.user)
        #     profileForm = ProfileForm(instance=userProfile)
        # except:
        #     profileForm = ProfileForm()
        ctx = {
            'form':ProfileForm()
        }
        return render(self.request,'profile/set_profile.html',ctx)

    def post(self,*args,**kwargs):
        form = ProfileForm(self.request.POST,self.request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return render(self.request,'profile/set_profile.html',{'form':form})



class UpdateProfileView(UpdateView):
    model = Profile
    fields = 'profile_pic','signiture','theme'
    template_name = 'profile/set_profile.html'

    def get_success_url(self):
        return reverse('home')


def UserProfile(request,*args,**kwargs):
    pk = kwargs['pk']
    return render(request,'profile/profile.html',{
        'user': Profile.objects.get(user=pk)
    })


class UpdatePwdView(View):
    def get(self,*args,**kwargs):
        ctx = {
            'form':PasswordChangeForm(self.request.user)
        }
        return render(self.request,'profile/changepwd.html',ctx)
    
    def post(self,*args,**kwargs):
        # username = self.request.POST['username']
        # user = User.objects.get(username=username)
        # if self.request.POST['password'] == self.request.POST['password2']:
        #     newPassword = self.request.POST['password']
        form = PasswordChangeForm(self.request.user,self.request.POST)
        if form.is_valid():
            user = form.save()
        else:
            ctx = {
                'msg':'Cannot find user from Backend',
                'form':form
            }
            return render(self.request,'profile/changepwd.html',ctx)
        if user is not None:
            update_session_auth_hash(self.request, user)
            # user.set_password(newPassword)
            return redirect("login")
        else:
            ctx = {
                'msg':'Cannot find user from Backend',
                'form':form
            }
            return render(self.request,'profile/changepwd.html',ctx)


class LogoutView(View):
    def get(self,*args,**kwargs):
        logout(self.request)