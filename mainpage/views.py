from django.http import HttpResponse
from django.shortcuts import render

def mainpage(request):
    return render(request, 'mainpage.html')

def new(request):
    return render(request, 'new.html')
    
def third(request):
    return render(request, 'third.html')


