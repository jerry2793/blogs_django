from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from django.views import View

# Create your views here.
# class HomePageView(View):
#     def get(self,*args,**kwargs):
#         return HttpResponse("Welcome!")
#     def post(self,*args,**kwargs):
#         return HttpResponse("POST to Homepage")

@login_required
def HomePageView(request,*args,**kwargs):
    ctx = {}
    return render(request,'homepage.html',ctx)