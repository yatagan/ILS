from django import forms
from core.models import BookInstance

class BookForm(forms.ModelForm):
    class Meta:
        model = BookInstance
        fields = ['book']
        
    number = forms.IntegerField()