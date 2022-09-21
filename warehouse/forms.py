from django import forms
from core.models import Book, BookInstance
from .models import Rack

class ManyBookInstancesForm(forms.Form):
    book = forms.ModelChoiceField(queryset=Book.objects.all())
    format_book = forms.ChoiceField(choices=BookInstance.FORMATS)
    number = forms.IntegerField()
    rack = forms.ModelChoiceField(queryset=Rack.objects.all())
