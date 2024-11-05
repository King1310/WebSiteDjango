from itertools import product
from lib2to3.fixes.fix_input import context

from django.http import HttpResponse
from django.shortcuts import render

from main.models import Category, Product
from unicodedata import category


def index(request):
    category = Category.objects.all()
    return render(request, 'main/index.html', {'category': category})

def contact(requset):
    category = Category.objects.all()
    return render(requset, 'main/contact.html', {'category': category})

def shop(requset):
    category = Category.objects.all() # извлекаем все категории
    product = Product.objects.all()
    return render(requset, 'main/shop.html', {'category': category, 'product': product})