from django.urls import path
from . import views


app_name = 'warehouse'
urlpatterns = [
    #warehouse`s main page`
    path('', views.index, name='index'),
    #add new_book
    path('new_book/', views.new_book, name='new_book'),
]