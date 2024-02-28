from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from girisimci.models import Girisimci


class GirisimciModelResource(resources.ModelResource):
    class Meta:
        model = Girisimci

class GirisimciModelAdmin(ImportExportModelAdmin):
    list_display = ('full_name', 'user_email','sirket_adi', 'created_at', 'updated_at', 'deleted_at')
    list_filter = ('is_active', 'is_deleted')
    list_display_links = ['user_email', 'full_name']
    search_fields = ['full_name', 'sirket_adi','user_email']
    
        # Arama bilgilendirme yazısı: 
    search_help_text = 'Arama Yapmak için burayı kullanabilirsiniz.'
    
    def user_email(self, obj):
        return obj.user.email

    user_email.short_description = 'Email'  # Set a custom column header
     # ImportExport:
    resource_class = GirisimciModelResource

admin.site.register(Girisimci, GirisimciModelAdmin)
