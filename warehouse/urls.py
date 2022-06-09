from django.urls import path
from . import views

app_name = 'warehouse'
urlpatterns = [
    #warehouse`s main page`
    path('', views.index, name='index'),
]