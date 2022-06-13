import numbers
from turtle import title
from typing import Any
from django.shortcuts import render,redirect

from core.models import *
from .forms import CardBookForm, VisitorForm, BookRentForm


def index(request):
    #library_reception home page
    return render(request, 'librery_reception/index.html')

def new_visitor(request):
    #Check visitor
    if request.method != 'POST':
        form = VisitorForm()
        context = {'form': form}
        return render(request, 'librery_reception/new_order.html', context)   
    else:
        if form.is_valid():
            form.save()
            return redirect(request, 'librery_reception/new_order.html')

def new_order(request):
    """Add new order from visitor"""
    exemlar_title = Book.objects.get(title)#треба дістати значення title
    exemplar_number = Book.objects.get(number)#треба дістати значення number
    if exemlar_title != Book(title):
        return f"Вибачте, такої книги не має в нашій бібліотеці"
    else:
        pass
    
    if exemplar_number > 0:
        form = BookRentForm()
        context = {'form': form} 
        return render(request, 'librery_reception/new_order.html', context)
    else:
        return f"Вибачте, цієї книги зараз не має в наявності"

def card_book_rent(request):
    #Change the form
    if request.method != 'POST':
        form = CardBookForm()
        context = {'form': form}
        return render(request, 'library_reception/card_book_rent.html', context)
    else:
        form = CardBookForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('library_reception:card_book_rent.html')
    

