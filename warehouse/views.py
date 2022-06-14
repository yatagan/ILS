from django.shortcuts import render,redirect
from .forms import BookForm


def index(request):
    #warehouse`s main page`
    return render(request, 'warehouse/index.html')

def new_book(request):
    #додати нову книгу
    #books = BookInstance.objects.get(id=book_id)
    if request.method != 'POST':
        form = BookForm()
    else:
        form = BookForm(data=request.POST)
        if form.is_valid():
            form.save()
            #for book in books:
                #book = form.save()
            return redirect('warehouse:index')
    context = {'form': form}
    return render(request, 'warehouse/new_book.html', context)