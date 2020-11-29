from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import *

urlpatterns = [
    # path('login/',LoginView.as_view(),name='login'),
    path('register/',RegisterView.as_view(),name='register'),
    # path('update/',UpdatePwdView.as_view(),name='update_pwd')
    path('profile_create/',login_required(SetProfileView.as_view()),name='create_profile'),
    path('profile_update<pk>/',login_required(UpdateProfileView.as_view()),name='update_profile'),
    path('profile_view<pk>/',UserProfile,name="author-page"),
]