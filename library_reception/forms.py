from django import forms
from core.models import BookRent

class CardBookForm(forms.ModelForm):
    class Meta:
        model = BookRent
        fields = ['books', 'visitor', 'date'] 


