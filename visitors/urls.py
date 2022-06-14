"""Patherns URL for visitors"""

import django
from django.urls import path, include

from . import views

app_name = 'visitors'
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    #Page of registrayion
    path('register/', views.register, name='register'),
]