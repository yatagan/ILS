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
        fields = ['book', 'format_book']
        label = {'book': 'Назва', 'format_book': 'Формат' }
