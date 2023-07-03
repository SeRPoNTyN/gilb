from django.urls import path
from .views import *


urlpatterns = [
    path("projects/", GetAllProjects.as_view(), name="all_projects"),
    path("about/", about, name="about"),
    path("project/<str:slug>", GetProject.as_view(), name="single_project"),
    path("contact/", contact, name="contact"),

    path("", Index.as_view(), name='home'),

]
