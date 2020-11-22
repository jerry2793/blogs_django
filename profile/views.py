from django.shortcuts import render
from django.views import View
from .models import Profile
from django.contrib.auth import authenticate

# Create your views here.
class LoginView(View):
    def __init__(self):
        self.template = {
            'login':'login.html'
        }

        self.ctx = {
            'form':LoginForm(self.request.POST)
        }


    def get(self,*args,**kwargs):
        return render(self.request,self.template['login'],self.ctx)
    
    def post(self,*args,**kwargs):
        user = self.request.user
        user = authenticate(username=user.username, password=user.password)
        if user is not None:
            return redirect('../')
        else:
            return render(self.request,self.template['login'],self.ctx)


class RegisterView(View):
    def get(self,*args,**kwargs):
        return render(self.request,self.template['register'],self.ctx)
