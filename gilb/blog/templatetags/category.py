from django import template
from django.db.models import *
from blog.models import *

register = template.Library()


@register.inclusion_tag("inc/categories_sidebar.html")
def get_categories_sidebar():
    categories = Category.objects.annotate(count=Count('post'))
    return {"categories": categories}
