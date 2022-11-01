from django.shortcuts import render, redirect
from core.models import BookInstance
from library_reception.models import BookInstanceRent, BookInstanceOrder
from library_reception.forms import BookInstanceOrderForm, BookInstanceRentForm, BookInstanceRentOrderForm
from visitors.models import Librarian, Member
from .models import BookInstanceOrder
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages
from django.core.paginator import Paginator

PAGE_ITEMS = 4

@login_required
def index(request):
    page = int(request.GET.get('page', '0'))
    paginator = Paginator(BookInstanceRent.objects.all(), PAGE_ITEMS)
    page_obj = paginator.get_page(page)

    context = {
        'page_obj': page_obj,
        'rents': BookInstanceRent.objects.all().order_by('member')[page * PAGE_ITEMS : page * PAGE_ITEMS + PAGE_ITEMS],
    }
    return render(request, 'library_reception/index.html', context)


@login_required
def show_order(request):
    if Librarian.objects.filter(id=request.user.id).exists():
        page = int(request.GET.get('page', '0'))
        paginator = Paginator(BookInstanceOrder.objects.all(), PAGE_ITEMS)
        page_pag = paginator.get_page(page)
        order_form = BookInstanceOrder.objects.all()[page * PAGE_ITEMS : page * PAGE_ITEMS + PAGE_ITEMS]
        context = {'order_form': order_form,
                    'page_pag': page_pag}
        return render(request, 'library_reception/show_order.html', context)
    else:
        return HttpResponse("У Вас не має таких прав", status=401)



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
                messages.success(request, "Книгу видано")
                return redirect('library_reception:index')

        context = {"rent_form": rent_form}
        return render(request, 'library_reception/book_rent.html', context)
    else:
        return HttpResponse("У Вас не має таких прав.", status=401)
        

@login_required
def rent_book_reserved(request):
    if Librarian.objects.filter(id=request.user.id).exists():
        if request.method != 'POST':
            rent_reserved_form = BookInstanceRentOrderForm
        else:
            rent_reserved_form = BookInstanceRentOrderForm(data=request.POST)
            if rent_reserved_form.is_valid():
                member = rent_reserved_form.cleaned_data['member']
                id_book_ordered = rent_reserved_form.cleaned_data['id_book_ordered']
                start_rent = rent_reserved_form.cleaned_data['start_rent']
                date_return = rent_reserved_form.cleaned_data['date_return']
                librarian=rent_reserved_form.cleaned_data['librarian']
                instance_ordered = BookInstance.objects.get(bookinstanceorder=id_book_ordered)
                
                rent = BookInstanceRent(
                    start_rent_date=start_rent,
                    return_date=date_return,
                    librarian=librarian,
                    member=member,
                )
                if instance_ordered.status == 'r':
                    rent.save()
                    instance_ordered.status = 'o'
                    instance_ordered.save()
                    rent.books.add(instance_ordered) 
                    messages.success(request, "Зарезервовану книгу видано")
                    return redirect('library_reception:book_rent')
                else:
                    messages.error(request, "Ця книга не була замовлена")
                    return redirect('library_reception:book_rent')   

        context = {'rent_reserved_form': rent_reserved_form}
        return render(request, 'library_reception/rent_book_reserved.html', context)        
    else:
        return HttpResponse("У Вас не має таких прав", status=401)            


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
                    book_instances = BookInstance.objects.filter(
                        book=book, status='a')
                    if len(book_instances) == 0:
                        order_form.add_error(
                            'books', f'Зараз "{ book.title }" не доступна для замовлення')
                        context = {'order_form': order_form}
                        return render(request, 'library_reception/book_order.html', context)
                    else:
                        book_instance = book_instances[0]
                        book_instance.status = 'r'
                        book_instance.save()
                        order.save()
                        order.books.add(book_instance)
                        messages.success(request, "Книгу зарезервовано.") 
                        return redirect('library_reception:book_order')

        context = {'order_form': order_form}
        return render(request, 'library_reception/book_order.html', context)

    else:
        return HttpResponse("У Вас не має таких прав.", status=401)
