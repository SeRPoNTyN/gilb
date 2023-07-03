from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import *
from .forms import *

# Create your views here.


class Index(ListView):
    model = Projects
    template_name = "main/index.html"
    context_object_name = "projects"

    def get_queryset(self):
        return Projects.objects.order_by("-created_at")[:5]


class GetProject(DetailView):
    model = Projects
    template_name = "main/single_project.html"
    context_object_name = "Project"

    def get_queryset(self):
        return Projects.objects.filter(slug=self.kwargs["slug"])


class GetAllProjects(ListView):
    model = Projects
    template_name = "main/all_projects.html"
    context_object_name = "projects"

    def get_queryset(self):
        return Projects.objects.order_by("-created_at")


def about(request):
    return render(request, template_name="main/about.html")


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            mail = send_mail(form.cleaned_data["subject"], form.cleaned_data["content"], "nector16@mail.ru", ["serpontynfunny@mail.ru"], fail_silently=False)
            if mail:
                messages.success(request, "Письмо отправлено!")
                return redirect("home")
            else:
                messages.error(request, "Ошибка отправки.")
                return redirect("contact")
        else:
            messages.error(request, "Ошибка валидации.")
    else:
        form = ContactForm()
    return render(request, "main/contact.html", {"form": form})

