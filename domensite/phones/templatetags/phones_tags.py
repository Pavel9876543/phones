from django import template
from phones.models import *

register = template.Library()

@register.simple_tag(name='getcats')
def get_categories():
    return Category.objects.all()

@register.simple_tag(name='filtcats')
def filt_categories():
    return Phones.objects.filter(pk__gte=2)

@register.inclusion_tag('phones/list_cats.html')
def show_categories(sort=None, cat_selected=''):
    if not sort:
        cats=Category.objects.all()
    else:
        cats=Category.objects.order_by(sort)
    return {'cats': cats, 'cat_selected': cat_selected}