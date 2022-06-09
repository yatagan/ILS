from django.urls import path

from . import views

app_name = 'ILS'
urlpatterns = [
    #Home page
    path('', views.index, name='index')
]