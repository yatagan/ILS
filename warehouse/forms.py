from django import forms
from core.models import Book, BookInstance
from .models import Rack

class BookForm(forms.ModelForm):
    class Meta:
        model = BookInstance
        fields = ['book']
        
    number = forms.IntegerField()

class ManyBookInstanceForm(forms.ModelForm):
    rack = forms.ModelChoiceField(queryset=Rack.objects.all())

    class Meta:
        model = BookInstance
        fields = ['book', 'format_book', 'isbn']

    number = forms.IntegerField()        