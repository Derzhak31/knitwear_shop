from django.views.generic import ListView, DetailView

from products.models import *
from products.utils import DataMixin


class Index(DataMixin, ListView):
    model = Product
    template_name = 'products/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_context(title='Главная страница')
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Product.objects.filter(is_index=True)


class Catalog(DataMixin, ListView):
    model = Product
    template_name = 'products/catalog.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_context(title='Каталог')
        return dict(list(context.items()) + list(c_def.items()))


class ShowProduct(DataMixin, DetailView):
    model = Product
    template_name = 'products/product.html'
    slug_url_kwarg = 'product_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_context(title=context['product'].name)
        return dict(list(context.items()) + list(c_def.items()))


class Payment(DataMixin, ListView):
    model = Product
    template_name = 'products/payment.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_context(title='Оплата')
        return dict(list(context.items()) + list(c_def.items()))


class Contacts(DataMixin, ListView):
    model = Product
    template_name = 'products/contacts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_context(title='Обратная связь')
        return dict(list(context.items()) + list(c_def.items()))
