from django.contrib import admin
from products.models import Product, ProductCategory, ProductBadge


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'price', 'sale', 'badge', 'is_index', 'time_update')
    list_display_links = ('name', 'category', 'time_update')
    search_fields = ('name', 'description')
    list_editable = ('badge', 'is_index')
    list_filter = ('category', 'badge', 'is_index')
    prepopulated_fields = {'slug': ('name',)}


class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_display_links = ('id', 'name')
    prepopulated_fields = {'slug': ('name',)}


class ProductBadgeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'color')
    list_display_links = ('id', 'name', 'color')
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductCategory, ProductCategoryAdmin)
admin.site.register(ProductBadge, ProductBadgeAdmin)
