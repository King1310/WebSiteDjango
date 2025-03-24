from itertools import product
from lib2to3.fixes.fix_input import context

from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, get_list_or_404

from main.models import Category, Product
from main.utils import q_search
from unicodedata import category


def index(request):
    category = Category.objects.all()
    return render(request, 'main/index.html', {'category': category})

def contact(requset):
    category = Category.objects.all()     # извлекаем все категории
    return render(requset, 'main/contact.html', {'category': category})

def shop(requset, category_slug = None):

    page = requset.GET.get('page', 1)
    query = requset.GET.get('q', None)

    category = None

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        product = Product.objects.filter(category=category)
    elif query:
        product = q_search(query)
    else:
        product = Product.objects.all()

    paginator = Paginator(product, 7)
    current_page = paginator.page(int(page))

    return render(requset, 'main/shop.html', {'category': category, 'product': current_page, 'slug_url': category_slug})

def product(request, product_slug):
    category = Category.objects.all()
    product = Product.objects.get(slug=product_slug)
    return render(request, 'main/shop/product.html', {'category': category, 'product': product})



