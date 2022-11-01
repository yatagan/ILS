
from django.forms.widgets import SelectDateWidget
from django import forms
from core.models import Book, BookInstance
from library_reception.models import BookInstanceOrder
from visitors.models import Librarian, Member
import datetime


class BookInstanceRentForm(forms.Form):
    books = forms.ModelMultipleChoiceField(
        queryset=BookInstance.objects.filter(status='a'), label="Книги:")
    librarian = forms.ModelChoiceField(queryset=Librarian.objects.all(
    ), label="Хто видав:", empty_label="Виберіть бібліотекаря")
    member = forms.ModelChoiceField(queryset=Member.objects.all(
    ), label="Хто получив:", empty_label="Виберіть користувача")
    start_rent_date = forms.DateField(
        widget=SelectDateWidget(), label="Дата початку аренди:")
    return_date = forms.DateField(
        widget=SelectDateWidget(), label="Дата повернення книги:")


class BookInstanceOrderForm(forms.Form):
    books = forms.ModelMultipleChoiceField(
        queryset=Book.objects.all(), label="Книги")
    member = forms.ModelChoiceField(queryset=Member.objects.all(
    ), label="Хто резервував", empty_label="Виберіть користувача")
    moment_reserve = forms.SplitDateTimeField(
        initial=datetime.datetime.now, label="Дата початку резервування", localize=True)


class BookInstanceRentOrderForm(forms.Form):
    member = forms.ModelChoiceField(
        queryset=Member.objects.all(), label="Хто замовив книгу")
    id_book_ordered = forms.IntegerField(label="Зарезервовані книги")
    librarian = forms.ModelChoiceField(
        queryset=Librarian.objects.all(), label="Хто оформив оренду")
    start_rent = forms.DateField(
        widget=SelectDateWidget(), label="Дата початку аренди:")
    date_return = forms.DateField(
        widget=SelectDateWidget(), label="Дата повернення книги:")    
