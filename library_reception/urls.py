from django.urls import path
from library_reception import views

app_name = 'library_reception'
urlpatterns = [
    #Library reception home page
    path('', views.index, name='index'),
    path('book_rent/', views.book_rent, name='book_rent'),
    path('book_order/', views.book_order, name='book_order'),
    path('show_order/', views.show_order, name='show_order'),
    path('show_response_order/', views.show_response_order, name='show_response_order'),
]
