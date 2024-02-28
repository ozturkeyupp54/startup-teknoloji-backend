from typing import Any
from django.contrib import admin
from django.db.models.fields.related import ForeignKey
from django.forms.models import ModelChoiceField
from django.http.request import HttpRequest
from post.models import Post
from author.models import Author
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from comment.admin import CommentInline

admin.site.site_header ='Startup Teknoloji Yazar/Admin Girişi'

class PostModelResource(resources.ModelResource):
    class Meta:
        model = Post

class PostModelAdmin(ImportExportModelAdmin):
    exclude = ('copyrightYear','_thumbnail_id','metadesc','pub_date','link','creator', 'categories', 'post_views_count','is_deleted','deleted_at')
    list_display = ('title', 'category', 'author', 'creator', 'categories', 'post_date', 'yayimlanma_durumu')
    list_filter = ('category',  'creator','categories', 'is_active', 'is_deleted')
    search_fields = ('title', 'content', 'creator')
    inlines = [CommentInline]
    
    # Arama bilgilendirme yazısı: 
    search_help_text = 'Arama Yapmak için burayı kullanabilirsiniz.'
    
    # ImportExport:
    resource_class = PostModelResource
    
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(author__user=request.user)
    
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
            if db_field.name == "author":
                # Show all authors for superusers
                if request.user.is_superuser:
                    kwargs["queryset"] = Author.objects.all()
                else:
                    # For regular users, show only their associated authors
                    kwargs["queryset"] = Author.objects.filter(user=request.user)
            return super().formfield_for_foreignkey(db_field, request, **kwargs)
    
    def has_import_permission(self, request, obj=None):
        # Check if the user is a superuser
        return request.user.is_superuser

    def has_export_permission(self, request, obj=None):
        # Check if the user is a superuser
        return request.user.is_superuser

admin.site.register(Post, PostModelAdmin)