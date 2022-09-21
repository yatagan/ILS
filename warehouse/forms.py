from django import forms
from core.models import BookInstance
from .models import Rack

class ManyBookInstancesForm(forms.ModelForm):
    rack = forms.ModelChoiceField(queryset=Rack.objects.all())

    class Meta:
        model = BookInstance
        fields = ['book', 'format_book']
        
    number = forms.IntegerField()