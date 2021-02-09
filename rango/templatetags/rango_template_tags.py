from django import template
from rango.models import Category

register = template.Library()

@register.inclusion_tag('rango/categories.html')
#function to get the list of categories to be used in menu
def get_category_list(current_category=None):
    return {'categories': Category.objects.all(),'current_category': current_category}
