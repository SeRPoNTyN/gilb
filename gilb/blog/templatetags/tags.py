from django import template
from django.db.models import *
from blog.models import *

register = template.Library()


@register.inclusion_tag("inc/tags_sidebar.html")
def get_tags_sidebar():
    tags = Tag.objects.all()
    return {"tags": tags}