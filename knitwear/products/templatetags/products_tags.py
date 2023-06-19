from django import template
from products.models import *

register = template.Library()


@register.simple_tag(name='getcats')
def get_categories():
    return ProductCategory.objects.all()
