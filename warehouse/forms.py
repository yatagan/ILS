from django import forms
from core.models import Book, BookInstance
from warehouse.models import Rack
from django.forms.widgets import SelectDateWidget
from visitors.models import Librarian


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


class ReturnInstanceForm(forms.Form):
    instance_id = forms.CharField(max_length=20, label="Введіть id книги ")
    date_return = forms.DateField(widget=SelectDateWidget(), label="Введіть дату повернення ")  
    librarian = forms.ModelChoiceField(queryset=Librarian.objects.all(), label="Хто прийняв ")  

