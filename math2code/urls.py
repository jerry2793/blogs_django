from django.contrib import admin
from django.urls import path

from .views import *

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',IndexView.as_view(),name='math2code-index'),
    path('articles/<int:pk>/',ArticlesView.as_view(),name='math2code-articles'),
]

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)