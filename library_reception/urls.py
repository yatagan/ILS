from django.urls import path
from . import views

app_name = 'library_reception'
urlpatterns = [
    #Library reception home page
    path('', views.index, name='index'),
    #form rent books
    path('card_book_rent/', views.card_book_rent, name='card_book_rent'),
]