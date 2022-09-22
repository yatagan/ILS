from django.urls import path
from . import views


app_name = 'warehouse'
urlpatterns = [
    #warehouse`s main page`
    path('', views.index, name='index'),
    #add new_book
    path('add_book_instance/', views.add_book_instance, name='add_book_instance'),
    #search books
    path('search_book/', views.search_book, name='search_book'),
    #search author
    path('search_author/', views.search_author, name='search_author'),
]