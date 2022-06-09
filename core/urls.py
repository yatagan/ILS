from django.urls import path
from . import views

app_name = 'core'
urlpatterns = [
    #main page
    path('', views.my_lib, name='my_lib'),
]