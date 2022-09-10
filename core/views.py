from dataclasses import dataclass
from django.shortcuts import render, redirect

from core.forms import BookInstanceForm
from .models import Book, BookInstance, Post
from django.db.models import Q



def index(request):
    """Home page library."""
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'core/index.html', context)

def search_books(request):
    search_query = request.GET.get('search', '')
    if search_query:
        books = Book.objects.filter(Q(title__icontains=search_query) | Q(authors__name__icontains=search_query)).distinct()
    else:
    #show all books
        books = Book.objects.all()
 
    context = {'books': books.order_by('title')}
    return render(request, 'core/search_results.html', context)

