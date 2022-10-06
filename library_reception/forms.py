from django.forms.widgets import SelectDateWidget
from django import forms
from core.models import Book, BookInstance
from library_reception.models import BookInstanceRent
from visitors.models import Member


class BookInstanceRentForm(forms.ModelForm):
    start_rent_date = forms.DateField(widget=SelectDateWidget(empty_label="Nothing"), label="Дата початку аренди:")   
    return_date = forms.DateField(widget=SelectDateWidget(empty_label="Nothing"), label="Дата повернення книги:")

    class Meta:
        model = BookInstanceRent
        fields = ['books', 'start_rent_date', 'return_date', 'librarian', 'member']

class BookInstanceOrderForm(forms.Form):
    books = forms.ModelMultipleChoiceField(queryset=Book.objects.all())
    member = forms.ModelChoiceField(queryset=Member.objects.all())
    #date_reserve = forms.DateTimeField(auto_now_add=False)

   