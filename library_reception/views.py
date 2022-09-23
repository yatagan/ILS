

from django.shortcuts import render, redirect
from core.models import BookInstance
from library_reception.models import BookInstanceRent
from library_reception.forms import BookInstanceOrderForm, BookInstanceRentForm


def index(request):
    #library_reception home page
    context = {'rents': BookInstanceRent.objects.all()}
    return render(request, 'library_reception/index.html', context)

def show_order(request):
    
    return render(request, 'library_reception/book_order.html')    

def book_rent(request):
    if request.method != 'POST':
        order_form = BookInstanceRentForm()
    else:
        order_form = BookInstanceRentForm(data=request.POST)
        if order_form.is_valid():
            order_form.save()
        return redirect('library_reception:index')
        
    context = {"order_form":order_form}
    return render(request, 'library_reception/book_rent.html', context)

def book_order(request):
    if request.method != 'POST':
        form_order = BookInstanceOrderForm()
    else:
        form_order = BookInstanceOrderForm(data=request.POST)
        if form_order.is_valid():
            stutus_query = form_order.cleaned_data['status']
            return redirect('library_reception:book_order')
        else:
            return {'form_order': 'Зараз ця книга не доступна для замовлення'}     

    context = {'form_order': form_order}
    return render(request, 'library_reception/book_order.html', context)               
           