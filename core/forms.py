from cProfile import label
from pyexpat import model
from django import forms
from .models import Book, BookInstance

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'authors', 'number']

class BookInstanceForm(forms.ModelForm):
    
    class Meta:
        model = BookInstance
        fields = ['book', 'date_lending', 'format_book', 'date_messege']
        label = {'book': 'Назва книги', 'date_lending': 'Дата видачи' }
