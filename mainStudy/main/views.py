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
    category = Category.objects.all()     # извлекаем все категории
    return render(requset, 'main/contact.html', {'category': category})

def shop(requset):
    product = Product.objects.all()
    return render(requset, 'main/shop.html', {'category': category, 'product': product})

def product(request, product_slug):
    category = Category.objects.all()
    product = Product.objects.get(slug=product_slug)
    return render(request, 'main/shop/product.html', {'category': category, 'product': product})

