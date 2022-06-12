from django.urls import path
from . import views

app_name = 'library_reception'
urlpatterns = [
    #Library reception home page
    path('', views.index, name='index'),
    #form rent books
    path('card_book_rent/<int:new_order_id>', views.card_book_rent, name='new_card'),
    #form new visitor 
    path('new_visitor/', views.new_visitor, name='new_visitor'),
    #form new order
    path('new_order/<int:new_visitor_id>', name='new_order'),
]