
from cProfile import label
from django.forms.widgets import SelectDateWidget
from django import forms
from .models import BookInstenceRent

# class CardBookForm(forms.ModelForm):
#     class Meta:
#         model = BookRent
#         fields = ['books', 'visitor', 'date']

# class VisitorForm(forms.ModelForm):
#     class Meta:
#         model = Visitor
#         fields = ['name', 'order'] 
#         labels = {'order': ''}

class BookInstenceRentForm(forms.ModelForm):
    title_book = forms.CharField(label="Назва книги")
    start_rent_date = forms.DateField(widget=SelectDateWidget(empty_label="Nothing"), label="Дата початку аренди:")   
    return_date = forms.DateField(widget=SelectDateWidget(empty_label="Nothing"), label="Дата повернення книги:")

    class Meta:
        model = BookInstenceRent
        fields = ['title_book', 'start_rent_date', 'return_date']
                




