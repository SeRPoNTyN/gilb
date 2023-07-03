from django.utils.safestring import mark_safe
from .models import *
from django import forms
from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class ProjectsAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Projects
        fields = '__all__'


class ProjectsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    form = ProjectsAdminForm
    save_as = True
    save_on_top = True
    list_display = ["id", "title", "slug", "get_main_image", "get_sub_image", "created_at"]
    list_display_links = ["id", "title"]
    search_fields = ["title", "description"]
    readonly_fields = ["get_main_image", "get_sub_image"]
    fields = ["title", "slug", "description", "main_image", "get_main_image", "sub_image", "get_sub_image", "created_at"]

    def get_main_image(self, obj):
        if obj.main_image:
            return mark_safe(f"<img src='{obj.main_image.url}' width ='50'>")
        return "-"

    get_main_image.short_description = "Main_Image"

    def get_sub_image(self, obj):
        if obj.sub_image:
            return mark_safe(f"<img src='{obj.sub_image.url}' width ='50'>")
        return "-"

    get_sub_image.short_description = "Sub_Image"


admin.site.register(Projects, ProjectsAdmin)
