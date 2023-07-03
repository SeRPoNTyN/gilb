from django.db import models
from django.urls import reverse


# Create your models here.


class Projects(models.Model):
    title = models.CharField(max_length=50, verbose_name="Title")
    slug = models.SlugField(max_length=60, verbose_name="Slug", unique=True)
    created_at = models.DateField(verbose_name="Date of creation")
    main_image = models.ImageField(upload_to="photos/%Y/%m/%d", verbose_name="Main Image")
    sub_image = models.ImageField(upload_to="photos/%Y/%m/%d", verbose_name="Subsidiary Image")
    description = models.TextField(verbose_name="Description")

    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"
        ordering = ['created_at']

    def get_absolute_url(self):
        return reverse("single_project", kwargs={"slug": self.slug})

    def __str__(self):
        return self.title


