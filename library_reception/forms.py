from django.forms.widgets import SelectDateWidget
from django import forms
from core.models import Book, BookInstance
from library_reception.models import BookInstanceRent, BookInstanceOrder
from visitors.models import Member


class BookInstanceRentForm(forms.ModelForm):
    start_rent_date = forms.DateField(widget=SelectDateWidget(empty_label="Nothing"), label="Дата початку аренди:")   
    return_date = forms.DateField(widget=SelectDateWidget(empty_label="Nothing"), label="Дата повернення книги:")

    class Meta:
        model = BookInstanceRent
        fields = ['books', 'start_rent_date', 'return_date', 'librarian', 'member']

class BookInstanceOrderForm(forms.Form):
    books = forms.ModelChoiceField(queryset=Book.objects.all())
    status = forms.ModelChoiceField(queryset=BookInstance.objects.all())
    member = forms.ChoiceField(choices=Member.objects.all())

    # class Meta:
    #     model = BookInstanceOrder
    #     fields = ['books', 'status', 'member']        
