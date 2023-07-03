from django import template
from main.models import *

register = template.Library()


@register.inclusion_tag("inc/get_recent_projects_single.html")
def get_recent_projects_single(cnt=3):
    recent_projects = Projects.objects.order_by("-created_at")[:cnt][::-1]
    return {"recent_projects": recent_projects, "cnt": cnt}