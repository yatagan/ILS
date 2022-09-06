from django.urls import path

from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'core'

urlpatterns = [
    #Home page
    path('', views.index, name='index'),
    #сторінка з книгами
    path('books/', views.books, name='books'),
    # path('new_order/', views.new_order, name='new_order'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)