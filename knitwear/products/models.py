from django.db import models
from django.urls import reverse


class ProductCategory(models.Model):
    name = models.CharField(max_length=128, unique=True, verbose_name='Наименование')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('products:category', kwargs={'category_slug': self.slug})

    class Meta:
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'


class ProductBadge(models.Model):
    name = models.CharField(max_length=16, unique=True, verbose_name='Текст')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    color = models.CharField(max_length=8, verbose_name='Цвет')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Плашку'
        verbose_name_plural = 'Плашки'


class Product(models.Model):
    name = models.CharField(max_length=256, verbose_name='Наименование', unique=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Цена')
    sale = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True, verbose_name='Цена со скидкой')
    image = models.ImageField(upload_to='product_images', verbose_name='Картинка')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    category = models.ForeignKey(to=ProductCategory, on_delete=models.PROTECT, verbose_name='Категория')
    badge = models.ForeignKey(to=ProductBadge, on_delete=models.PROTECT, null=True, blank=True, verbose_name='Плашка')
    is_index = models.BooleanField(default=False, verbose_name='На главном экране')

    def __str__(self):
        return f'Продукт: {self.name} | Категория: {self.category.name}'

    def get_absolute_url(self):
        return reverse('products:product', kwargs={'product_slug': self.slug})

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['time_update']
