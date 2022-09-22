from django import forms
from core.models import Book, BookInstance
from warehouse.models import Rack

class AddBookInstanceForm(forms.Form):
    book = forms.ModelChoiceField(queryset=Book.objects.all())
    status = forms.ChoiceField(choices=BookInstance.LOAN_STATUS)
    format_book = forms.ChoiceField(choices=BookInstance.FORMATS)
    number = forms.IntegerField()
    isbn = forms.CharField()
    rack = forms.ModelChoiceField(queryset=Rack.objects.all())




       

   