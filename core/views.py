from django.shortcuts import render, redirect
from .models import Book 
from .forms import BookForm


def index(request):
    """Home page app ILS."""
    return render(request, 'ILS/index.html')
    