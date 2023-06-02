from django.shortcuts import render
from products.models import Product, ProductCategory, ProductBadge


def index(request):
    context = {
        'title': 'Зайцева',
        'products': Product.objects.all(),
        'badge': ProductBadge.objects.all(),
    }
    return render(request, 'products/index.html', context)


def products(request):
    context = {
        'title': 'Каталог',
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all(),
        'badge': ProductBadge.objects.all(),
    }
    return render(request, 'products/products.html', context)

