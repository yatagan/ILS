from django.forms.widgets import SelectDateWidget
from django import forms
from .models import BookInstanceRent


class BookInstanceRentForm(forms.ModelForm):
    start_rent_date = forms.DateField(widget=SelectDateWidget(empty_label="Nothing"), label="Дата початку аренди:")   
    return_date = forms.DateField(widget=SelectDateWidget(empty_label="Nothing"), label="Дата повернення книги:")

    class Meta:
        model = BookInstanceRent
        fields = ['books', 'start_rent_date', 'return_date']
