from django.shortcuts import render, redirect
from core.models import BookInstance
from library_reception.models import BookInstanceRent, BookInstanceOrder
from library_reception.forms import BookInstanceOrderForm, BookInstanceRentForm
from visitors.models import Librarian, Member
from .models import BookInstanceOrder
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


@login_required
def index(request):
    #library_reception home page
    context = {'rent_form': BookInstanceRent.objects.all()}
    return render(request, 'library_reception/index.html', context)

@login_required
def show_order(request):
    if Librarian.objects.filter(id=request.user.id).exists():
            order_form = BookInstanceOrder.objects.all()
            context = {'order_form': order_form}
            return render(request, 'library_reception/show_order.html', context) 
    else: 
<        return HttpResponse("У Вас не має таких прав", status=401)

        
@login_required
def show_response_order(request):
    return render(request, 'library_reception/show_response_order.html')          


@login_required
def book_rent(request):
    if Librarian.objects.filter(id=request.user.id).exists():
        if request.method != 'POST':
            rent_form = BookInstanceRentForm()
        else:
            rent_form = BookInstanceRentForm(data=request.POST)
            if rent_form.is_valid():
                book_instances = rent_form.cleaned_data['books']
                member = rent_form.cleaned_data['member']
                rent = BookInstanceRent(
                    start_rent_date=rent_form.cleaned_data['start_rent_date'],
                    return_date=rent_form.cleaned_data['return_date'],
                    librarian=rent_form.cleaned_data['librarian'],
                    member=member,
                )
                rent.save()

                for book_instance in book_instances:
                    book_instance.status = 'o'
                    book_instance.save()
                    rent.books.add(book_instance)
                
                return redirect('library_reception:index')
    
        context = {"rent_form":rent_form}
        return render(request, 'library_reception/book_rent.html', context)
    else: 
        return HttpResponse("У Вас не має таких прав.", status=401)

@login_required
def book_order(request):
    if Member.objects.filter(id=request.user.id).exists():
        if request.method != 'POST':
            order_form = BookInstanceOrderForm()
        else:
            order_form = BookInstanceOrderForm(data=request.POST)
            if order_form.is_valid():
                books = order_form.cleaned_data['books']
                member = order_form.cleaned_data['member']
                order = BookInstanceOrder(
                    member=member,
                    moment_reserve=order_form.cleaned_data['moment_reserve'], 
                )
                for book in books:
                    book_instances = BookInstance.objects.filter(book=book, status='a')
                    if len(book_instances) == 0: 
                        order_form.add_error('books', f'Зараз "{book.title}" не доступна для замовлення')
                        context = {'order_form': order_form}
                        return render(request, 'library_reception/book_order.html', context)
                    else:   
                        book_instance = book_instances[0]
                        book_instance.status = 'r'
                        book_instance.save()
                        order.save()
                        order.books.add(book_instance)
                        return redirect('library_reception:show_response_order')
                            
        context = {'order_form': order_form}
        return render(request, 'library_reception/book_order.html', context) 

    else: 
        return HttpResponse("У Вас не має таких прав.", status=401)