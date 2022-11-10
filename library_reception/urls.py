from django.urls import path
from . import views

app_name = 'library_reception'
urlpatterns = [
    # Library reception home page
    path('', views.index, name='index'),
    path('book_rent/', views.book_rent, name='book_rent'),
    path('book_order/', views.book_order, name='book_order'),
    path('show_order/', views.show_order, name='show_order'),
    path('rent_book_reserved/', views.rent_book_reserved, name='rent_book_reserved'),
    path('check_time_order', views.check_time_order, name='check_time_order'),
]
