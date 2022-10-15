
from django.forms.widgets import SelectDateWidget
from django import forms
from core.models import Book, BookInstance
from library_reception.models import BookInstanceOrder, BookInstanceRent
from visitors.models import Librarian, Member


class BookInstanceRentForm(forms.Form):
    books = forms.ModelMultipleChoiceField(queryset=BookInstance.objects.filter(status='a'), label="Книги:")
    librarian = forms.ModelChoiceField(queryset=Librarian.objects.all(), label="Хто видав:", empty_label="Виберіть бібліотекаря")
    member = forms.ModelChoiceField(queryset=Member.objects.all(), label="Хто получив:", empty_label="Виберіть користувача")
    start_rent_date = forms.DateField(widget=SelectDateWidget(), label="Дата початку аренди:")   
    return_date = forms.DateField(widget=SelectDateWidget(), label="Дата повернення книги:")


class BookInstanceOrderForm(forms.Form):
    books = forms.ModelMultipleChoiceField(queryset=Book.objects.all(), label="Книги")
    member = forms.ModelChoiceField(queryset=Member.objects.all(), label="Хто резервував", empty_label="Виберіть користувача")
    date_start_reserve = forms.DateTimeField(widget=SelectDateWidget, label="Дата початку резервування")

    class Meta:
        model = BookInstanceOrder
        fields = ['books', 'date_start_reserve', 'member']


   