from django.urls import path
from . import views

app_name = 'library_reception'
urlpatterns = [
    # Library reception home page
    path('', views.index, name='index'),
    path('book_lending/', views.book_lending, name='book_lending'),
    path('book_reservation/', views.book_reservation, name='book_reservation'),
    path('show_reservation/', views.show_reservation, name='show_reservation'),
    path('lending_book_reserved/', views.lending_book_reserved, name='lending_book_reserved'),
    path('check_time_order', views.check_time_order, name='check_time_order'),
]
