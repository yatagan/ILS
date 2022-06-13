
from dataclasses import field
from django import forms
from core.models import *

class CardBookForm(forms.ModelForm):
    class Meta:
        model = BookRent
        fields = ['books', 'visitor', 'date']

class VisitorForm(forms.ModelForm):
    class Meta:
        model = Visitor
        field = ['name', 'order'] 
        labels = {'order': ''}

class BookRentForm(forms.ModelForm):
    class Meta:
        model = BookRent, BookInstance
        field = ['books', 'visitor', 'order', 'date-on', 'date-off']
                




