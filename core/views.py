from django.shortcuts import render
from .models import Book 
from .forms import BookForm


def index(request):
    """Home page library."""
    return render(request, 'core/index.html')

    