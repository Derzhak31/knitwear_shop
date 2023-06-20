from django.shortcuts import render, get_object_or_404
from products.models import *

menu = [
    {'title': 'Главная', 'url_name': 'index'},
    {'title': 'Каталог', 'url_name': 'products:index'},
    {'title': 'Оплата', 'url_name': 'payment'},
    {'title': 'Контакты', 'url_name': 'contacts'}
]


def index(request):
    context = {
        'menu': menu,
        'title': 'Главная',
        'products': Product.objects.all(),
    }
    return render(request, 'products/index.html', context)


def catalog(request):
    context = {
        'menu': menu,
        'title': 'Каталог',
        'products': Product.objects.all(),
    }
    return render(request, 'products/catalog.html', context)


def show_product(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug)
    context = {
        'product': product,
        'title': product.name,
        'category': product.category.name,
    }
    return render(request, 'products/product.html', context)


def payment(request):
    context = {
        'menu': menu,
        'title': 'Оплата',
    }
    return render(request, 'products/payment.html', context)


def contacts(request):
    context = {
        'menu': menu,
        'title': 'Контакты',
    }
    return render(request, 'products/contacts.html', context)
