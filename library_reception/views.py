
from django.shortcuts import render, redirect
from core.models import *
from core.forms import BookInstanceForm 
# from .forms import VisitorForm, BookRentForm


def index(request):
    #library_reception home page
    return render(request, 'library_reception/index.html')

def new_order(request):
    if request.method != 'POST':
        form = BookInstanceForm()
    else:
        form = BookInstanceForm(data=request.POST)
        if form.is_valid():
            form.save()
            print (form)
            return redirect('library_reception:new_order')    
   
    context = {'form': form}
    return render(request, 'library_reception/index.html', context)   

# def new_visitor(request):
#     #Check visitor
#     if request.method != 'POST':
#         form = VisitorForm()
#         context = {'form': form}
#         return render(request, 'librery_reception/new_order.html', context)   
#     else:
#         if form.is_valid():
#             form.save()
#             return redirect(request, 'librery_reception/new_order.html')


#def card_book_rent(request):
    #Change the form
    # if request.method != 'POST':
    #     form = CardBookForm()
    #     context = {'form': form}
    #     return render(request, 'library_reception/card_book_rent.html', context)
    # else:
    #     form = CardBookForm(data=request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('library_reception:card_book_rent.html')
    

