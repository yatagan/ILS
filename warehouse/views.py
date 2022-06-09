from django.shortcuts import render

def index(request):
    #warehouse`s main page`
    return render(request, 'warehouse/index.html')