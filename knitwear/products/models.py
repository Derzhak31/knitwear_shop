from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class ProductBadge(models.Model):
    name = models.CharField(max_length=16, unique=True)
    color = models.CharField(max_length=8)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    sale = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    image = models.ImageField(upload_to='product_images')
    category = models.ForeignKey(to=ProductCategory, on_delete=models.PROTECT)
    badge = models.ForeignKey(to=ProductBadge, on_delete=models.PROTECT, null=True, blank=True)
    # quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'Продукт: {self.name} | Категория: {self.category.name}'
