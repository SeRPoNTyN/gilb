from django.utils.safestring import mark_safe
from .models import *
from django import forms
from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget
# Register your models here.


class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    save_as = True
    save_on_top = True
    list_display = ["id", "title", "slug"]
    list_display_links = ["id", "title"]
    search_fields = ["title"]
    fields = ["title", "slug"]


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    save_as = True
    save_on_top = True
    list_display = ["id", "title", "slug"]
    list_display_links = ["id", "title"]
    search_fields = ["title"]
    fields = ["title", "slug"]


class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Post
        fields = '__all__'


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    form = PostAdminForm
    save_as = True
    save_on_top = True
    list_display = ["id", "title", "slug", "get_image", "created_at"]
    list_display_links = ["id", "title"]
    search_fields = ["title", "content"]
    list_filter = ["category", "tags"]
    readonly_fields = ["get_image", "views", "created_at"]
    fields = ["title", "slug", "content", "tags", "category", "image", "get_image", "created_at", "views"]

    def get_image(self, obj):
        if obj.image:
            return mark_safe(f"<img src='{obj.image.url}' width ='50'>")
        return "-"

    get_image.short_description = "Image"


admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Category, CategoryAdmin)

