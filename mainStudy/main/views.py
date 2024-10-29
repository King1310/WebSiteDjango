from lib2to3.fixes.fix_input import context

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'main/index.html')

def contact(requset):
    return render(requset, 'main/contact.html')

def shop(requset):
    return render(requset, 'main/shop.html')