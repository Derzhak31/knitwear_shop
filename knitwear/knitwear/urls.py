from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from products.views import index, contacts, payment

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('payment/', payment, name='payment'),
    path('contacts/', contacts, name='contacts'),
    path('products/', include('products.urls')),
    path('users/', include('users.urls', namespace='users')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
