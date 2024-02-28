from django.contrib import admin
from .models import Author
from import_export import resources
from import_export.admin import ImportExportModelAdmin



class AuthorModelResource(resources.ModelResource):
    class Meta:
        model = Author


class AuthorModelAdmin(ImportExportModelAdmin):
    exclude = ('slug', 'deleted_at', 'is_active', 'is_deleted')
    list_display = ('full_name', 'user_email', 'created_at', 'updated_at')
    list_filter = ('is_active', 'is_deleted')
    search_fields = ['full_name', 'user__email']  # Use '__' to traverse relationships

        
     # ImportExport:
    resource_class = AuthorModelResource
    
    def user_email(self, obj):
        return obj.user.email

    user_email.short_description = 'Email'  # Set a custom column header

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        # If the user is not a superuser, filter the queryset to show only the author associated with the logged-in user
        if not request.user.is_superuser:
            return qs.filter(user=request.user)
        return qs

admin.site.register(Author, AuthorModelAdmin)
