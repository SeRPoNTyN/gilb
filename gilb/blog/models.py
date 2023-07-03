from django.db import models
from django.urls import reverse


# Create your models here.


class Tag(models.Model):
    title = models.CharField(max_length=50, verbose_name="Title")
    slug = models.SlugField(max_length=50, verbose_name="Slug", unique=True)

    def get_absolute_url(self):
        return reverse("blog_by_tags", kwargs={"slug": self.slug})

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"
        ordering = ['title']

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=50, verbose_name="Title")
    slug = models.SlugField(max_length=50, verbose_name="Slug", unique=True)

    def get_absolute_url(self):
        return reverse("blog_by_categories", kwargs={"slug": self.slug})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ['title']


class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name="Title")
    slug = models.SlugField(max_length=50, verbose_name="Slug", unique=True)
    content = models.TextField(verbose_name="Content")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")
    views = models.IntegerField(default=0, verbose_name="Views")
    tags = models.ManyToManyField(Tag, verbose_name="Tags")
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name="Category")
    image = models.ImageField(upload_to="photos/%Y/%m/%d", verbose_name="Image")

    def get_absolute_url(self):
        return reverse("single_post", kwargs={"slug": self.slug})

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class Comment(models.Model):
    name = models.CharField(max_length=50, verbose_name="Name")
    comment = models.TextField(verbose_name="Comment")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")
    post = models.ForeignKey(Post, on_delete=models.PROTECT, verbose_name="Post")

    def __str__(self):
        return f"{self.name} comment"

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
        ordering = ['-created_at']

