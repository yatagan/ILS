from django.urls import path
from . import views


app_name = 'warehouse'
urlpatterns = [
    #warehouse`s main page`
    path('', views.index, name='index'),
    #add new_book
    path('new_item_book/', views.new_item_book, name='new_item_book'),
    #search books
    path('search_book/', views.search_book, name='search_book'),
    #search author
    path('search_author/', views.search_author, name='search_author'),
    path('list_items/', views.list_items, name="list_items")
]