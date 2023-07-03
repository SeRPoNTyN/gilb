from django import template
from django.db.models import *
from blog.models import *

register = template.Library()


@register.inclusion_tag("inc/recent_posts_sidebar.html")
def get_recent_posts_sidebar(cnt=4):
    posts = Post.objects.order_by("-created_at")[:cnt]
    return {"posts": posts}


@register.inclusion_tag("inc/preview_and_next_post.html")
def get_prev_and_next_posts(post):
    has_next = False
    has_preview = False
    next_post = 0
    preview_post = 0
    if post.id < Post.objects.all().count():
        next_post = Post.objects.get(pk=post.id+1)
        has_next = True
    if post.id > 1:
        preview_post = Post.objects.get(pk=post.id-1)
        has_preview = True
    return {"preview_post": preview_post, "next_post": next_post, "has_next": has_next, "has_preview": has_preview}
