from django.urls import path
from .views import *


urlpatterns = [
    path("", GetAllPosts.as_view(), name="blog"),
    path("category/<str:slug>", PostsByCategories.as_view(), name="blog_by_categories"),
    path("post/<str:slug>", GetPost.as_view(), name="single_post"),
    path("add_comment/<str:slug>", add_comment, name="add_comment")
]
