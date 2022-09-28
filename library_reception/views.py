

from django.shortcuts import render, redirect
from core.models import BookInstance
from library_reception.models import BookInstanceRent
from library_reception.forms import BookInstanceOrderForm, BookInstanceRentForm
from .models import BookInstanceOrder
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import Http404


def index(request):
    #library_reception home page
    #context = {'rents': BookInstanceRent.objects.all()}
    return render(request, 'library_reception/index.html') #context)

@login_required
def show_order(request):
    permitions = User.objects.filter(is_staff=1)
    for legal_user in permitions:
        if request.user == legal_user:
            return render(request, 'library_reception/book_order.html') 
    else:
         raise Http404        



@login_required
def book_rent(request):
    permitions = User.objects.filter(is_staff=1)
    for legal_user in permitions:
        if request.user == legal_user:
            if request.method != 'POST':
                order_form = BookInstanceRentForm()
            else:
                order_form = BookInstanceRentForm(data=request.POST)
                if order_form.is_valid():
                    order_form.save()
                    return redirect('library_reception:index')
        
            context = {"order_form":order_form}
            return render(request, 'library_reception/book_rent.html', context)
    else:
         raise Http404

@login_required
def book_order(request):
    if request.method != 'POST':
        form_order = BookInstanceOrderForm()
    else:
        form_order = BookInstanceOrderForm(data=request.POST)
        if form_order.is_valid():
            books = form_order.cleaned_data['books']
            member = form_order.cleaned_data['member']

            order = BookInstanceOrder(member=member)
            order.save()
            for book in books:
                book_instances = BookInstance.objects.filter(book=book, status='a')
                if len(book_instances) == 0:
                    form_order.add_error('books', f'Зараз {book.title} не доступна для замовлення')
                    context = {'form_order': form_order}
                    return render(request, 'library_reception/book_order.html', context)  
                book_instance = book_instances[0]
                book_instance.status = 'r'
                book_instance.save()
                order.books.add(book_instance)

    context = {'form_order': form_order}
    return render(request, 'library_reception/book_order.html', context)               
           