from django import forms
from .models import Book, BookInstance
from visitors.models import Member


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'authors', 'number']


class BookInstanceForm(forms.ModelForm):

    class Meta:
        model = BookInstance
        fields = ['book', 'format_book', 'status']
