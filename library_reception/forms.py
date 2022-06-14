

from django import forms
from core.models import *

class CardBookForm(forms.ModelForm):
    class Meta:
        model = BookRent
        fields = ['books', 'visitor', 'date']

class VisitorForm(forms.ModelForm):
    class Meta:
        model = Visitor
        fields = ['name', 'order'] 
        labels = {'order': ''}

# class BookRentForm(forms.ModelForm):
#     class Meta:
#         model = BookRent
#         fields = ['books', 'visitor', 'order', 'date']
                




