from django.urls import path
from products.views import Catalog, ShowProduct

app_name = 'products'

urlpatterns = [
    path('', Catalog.as_view(), name='index'),
    path('<slug:product_slug>/', ShowProduct.as_view(), name='product'),
]
