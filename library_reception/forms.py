from asyncio.windows_events import NULL
from cProfile import label
from tabnanny import verbose
from django.forms.widgets import SelectDateWidget
from django import forms
from core.models import Book, BookInstance
from library_reception.models import BookInstanceOrder, BookInstanceRent
from visitors.models import Member


class BookInstanceRentForm(forms.ModelForm):
    books = forms.ModelMultipleChoiceField(queryset=BookInstance.objects.filter(status='a'), label="Книги:")
    member = forms.ModelChoiceField(queryset=Member.objects.all(), label="Хто получив:")
    start_rent_date = forms.DateField(widget=SelectDateWidget(empty_label="Nothing"), label="Дата початку аренди:")   
    return_date = forms.DateField(widget=SelectDateWidget(empty_label="Nothing"), label="Дата повернення книги:")

    class Meta:
        model = BookInstanceRent
        fields = ['books', 'start_rent_date', 'return_date', 'librarian', 'member']

class BookInstanceOrderForm(forms.Form):
    books = forms.ModelMultipleChoiceField(queryset=Book.objects.all(), label="Книги")
    member = forms.ModelChoiceField(queryset=Member.objects.all(), label="Хто резервував")
    date_start_reserve = forms.DateTimeField(widget=SelectDateWidget(empty_label="Nothing"), label="Дата початку резервування")

    class Meta:
        model = BookInstanceOrder
        fields = ['books', 'date_start_reserve', 'member']


   