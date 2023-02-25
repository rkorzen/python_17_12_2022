from django.contrib import admin
from import_export import resources
from .models import Post
from import_export.admin import ExportMixin, ImportExportMixin


class PostResource(resources.ModelResource):
    class Meta:
        model = Post


# Register your models here.
@admin.register(Post)
class PostAdmin(ImportExportMixin, admin.ModelAdmin):
    readonly_fields = ["created", "modified"]
    resource_class = PostResource
