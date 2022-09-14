from django.urls import path
from . import views

app_name = 'library_reception'
urlpatterns = [
    #Library reception home page
    path('', views.index, name='index'),
    path('book_rent/', views.book_rent, name='book_rent'),
    #form new order
    path('new_order/', views.new_order, name='new_order'),
]