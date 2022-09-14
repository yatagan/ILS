
from django.shortcuts import render, redirect
from library_reception.models import BookInstanceRent
from library_reception.forms import BookInstanceRentForm


def index(request):
    #library_reception home page
    return render(request, 'library_reception/index.html', {'rents': BookInstanceRent.objects.all()})

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
           