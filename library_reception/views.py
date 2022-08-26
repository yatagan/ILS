
from django.shortcuts import render,redirect
from core.models import *
from .forms import VisitorForm #, BookRentForm


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
    
    exemplar_title = Book.objects.get(title)#треба дістати значення title
    exemplar_number = Book.objects.get(number)#треба дістати значення number
    
    
    if exemplar_number > 0:
        form = BookRentForm()
        context = {'form': form} 
        return render(request, 'librery_reception/new_order.html', context)
    else:
        return f"Вибачте, цієї книги зараз не має в наявності"

#def card_book_rent(request):
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
    

