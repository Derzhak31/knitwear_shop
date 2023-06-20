from django.urls import path
from products.views import *

app_name = 'products'

urlpatterns = [
    path('', catalog, name='index'),
    path('<slug:product_slug>/', show_product, name='product'),
]
