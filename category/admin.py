from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from category.models import Category

class CategoryModelResource(resources.ModelResource):
    class Meta:
        model = Category

class CategoryModelAdmin(ImportExportModelAdmin):
    list_display = ('name', 'created_at', 'updated_at', 'deleted_at')
    list_filter = ('is_active', 'is_deleted')
    search_fields = ['name']
 
        # ImportExport:
    resource_class = CategoryModelResource
    
admin.site.register(Category, CategoryModelAdmin)
