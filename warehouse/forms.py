from django import forms
from core.models import Book, BookInstance
from warehouse.models import Rack


class BookForm(forms.ModelForm):
    class Meta:
        model = BookInstance
        fields = ['book']
        
    number = forms.IntegerField()




class AddBookInstanceForm(forms.Form):
    book = forms.ModelChoiceField(queryset=Book.objects.all(), label="Назва книги ")
    status = forms.ChoiceField(choices=BookInstance.LOAN_STATUS, label="Статус книги ")
    format_book = forms.ChoiceField(choices=BookInstance.FORMATS, label="Формат книги ")
    number = forms.IntegerField(label="Кількість книг ")
    isbn = forms.CharField(label="ISBN ")
    rack = forms.ModelChoiceField(queryset=Rack.objects.all(), label="Назва полички ")




       

   
