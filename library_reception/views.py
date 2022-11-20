from django.shortcuts import render, redirect
from core.models import BookInstance
from library_reception.models import BookLending, BookReservation
from library_reception.forms import BookReservationForm, BookLendingForm, BookLendingInstanceReservedForm
from visitors.models import Librarian, Member
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
from django.contrib import messages
from django.core.paginator import Paginator
from datetime import timedelta
from django.utils import timezone

PAGE_ITEMS = 5

@login_required
def index(request):
    page = int(request.GET.get('page', '0'))
    paginator = Paginator(BookLending.objects.all(), PAGE_ITEMS)
    page_obj = paginator.get_page(page)

    context = {'page_obj': page_obj}
    return render(request, 'library_reception/index.html', context)


@login_required
def show_reservation(request):
    if Librarian.objects.filter(id=request.user.id).exists():
        page = int(request.GET.get('page', '0'))
        paginator = Paginator(BookReservation.objects.all(), PAGE_ITEMS)
        page_pag = paginator.get_page(page)
        context = {'page_pag': page_pag}
        return render(request, 'library_reception/show_reservation.html', context)
    else:
        return HttpResponse("У Вас не має таких прав", status=401)



@login_required
def book_lending(request):
    if Librarian.objects.filter(id=request.user.id).exists():
        if request.method != 'POST':
            rent_form = BookLendingForm()
        else:
            rent_form = BookLendingForm(data=request.POST)
            if rent_form.is_valid():
                book_instances = rent_form.cleaned_data['books']
                member = rent_form.cleaned_data['member']
                rent = BookLending(
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
        return render(request, 'library_reception/book_lending.html', context)
    else:
        return HttpResponse("У Вас не має таких прав.", status=401)
        

@login_required
def lending_book_reserved(request):
    if Librarian.objects.filter(id=request.user.id).exists():
        if request.method != 'POST':
            rent_reserved_form = BookLendingInstanceReservedForm
        else:
            rent_reserved_form = BookLendingInstanceReservedForm(data=request.POST)
            if rent_reserved_form.is_valid():
                member = rent_reserved_form.cleaned_data['member']
                id_book_ordered = rent_reserved_form.cleaned_data['id_book_ordered']
                start_rent = rent_reserved_form.cleaned_data['start_rent']
                date_return = rent_reserved_form.cleaned_data['date_return']
                librarian=rent_reserved_form.cleaned_data['librarian']
                instance_ordered = BookInstance.objects.get(bookinstanceorder=id_book_ordered)
                
                rent = BookLending(
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
                    return redirect('library_reception:book_lending')
                else:
                    messages.error(request, "Ця книга не була замовлена")
                    return redirect('library_reception:book_lending')   

        context = {'rent_reserved_form': rent_reserved_form}
        return render(request, 'library_reception/lending_book_reserved.html', context)        
    else:
        return HttpResponse("У Вас не має таких прав", status=401)            


@login_required
def book_reservation(request):
    if Member.objects.filter(id=request.user.id).exists():
        if request.method != 'POST':
            order_form = BookReservationForm()
        else:
            order_form = BookReservationForm(data=request.POST)
            if order_form.is_valid():
                books = order_form.cleaned_data['books']
                member = order_form.cleaned_data['member']
                order = BookReservation(
                    member=member,
                    moment_reserve=order_form.cleaned_data['moment_reserve'],
                )
                order.save()
                for book in books:
                    book_instances = BookInstance.objects.filter(
                        book=book, status='a')
                    if len(book_instances) == 0:
                        order_form.add_error(
                            'books', f'Зараз "{ book.title }" не доступна для замовлення')
                        context = {'order_form': order_form}
                        return render(request, 'library_reception/book_reservation.html', context)
                    else:
                        book_instance = book_instances[0]
                        book_instance.status = 'r'
                        book_instance.save()
                        order.books.add(book_instance)
                        messages.success(request, "Книгу зарезервовано.")
                        return redirect('library_reception:book_reservation')
                
        context = {'order_form': order_form}
        return render(request, 'library_reception/book_reservation.html', context)

    else:
        return HttpResponse("У Вас не має таких прав.", status=401)


def check_time_order(request):
    today = timezone.now()
    day_plus = timedelta(days=2)
    orders = BookReservation.objects.all()
    for order in orders:
        if order.moment_reserve + day_plus < today:
            for book_instance in order.books.all():
                book_instance.status = 'a'
                book_instance.save()
    messages.success(request, "Замовлення книг анульовані")
    return redirect('library_reception:show_reservation') 

