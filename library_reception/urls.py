from django.urls import path
from . import views

app_name = 'library_reception'
urlpatterns = [
    #Library reception home page
    path('', views.index, name='index'),
    #form new visitor 
    # path('new_visitor/', views.new_visitor, name='new_visitor'),
    #form new order
    path('new_order/', views.new_order, name='new_order'),
]