from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from girisim.models import Girisim, GirisimHaberleri, GirisimGelismelerHedefler, GirisiminYatirimTurlari


class GirisimHaberleriInline(admin.TabularInline):
    model = GirisimHaberleri
    extra = 0  # Number of empty attachment forms to display


class GirisimHaberleriAdmin(admin.ModelAdmin):
    list_display = ('haber_basligi', 'haberin_ilgili_oldugu_girisim','is_active', 'is_deleted')
    list_filter = ('is_active', 'is_deleted')
    search_fields = ('haber_basligi', 'haberin_ilgili_oldugu_girisim')
    
class GirisimGelismelerHedeflerInline(admin.TabularInline):
    model = GirisimGelismelerHedefler
    extra = 0  # Number of empty attachment forms to display


class GirisimGelismelerHedeflerAdmin(admin.ModelAdmin):
    list_display = ('gelisme_veya_hedef_aciklamasi', 'target_to_girisim','is_active', 'is_deleted')
    list_filter = ('is_active', 'is_deleted')
    search_fields = ('gelisme_veya_hedef_aciklamasi', 'target_to_girisim')
    

class GirisiminYatirimTurlariInline(admin.TabularInline):
    model = GirisiminYatirimTurlari
    extra = 0  # Number of empty attachment forms to display


class GirisiminYatirimTurlariAdmin(admin.ModelAdmin):
    list_display = ('yatirimin_ilgili_oldugu_girisim','round_tipi','is_active', 'is_deleted')
    list_filter = ('is_active', 'is_deleted')
    search_fields = ('round_tipi', 'yatirimin_ilgili_oldugu_girisim')


class GirisimModelResource(resources.ModelResource):
    class Meta:
        model = Girisim

class GirisimAdmin(ImportExportModelAdmin):
    list_display = ('get_girisimci_full_name','girisim_adi', 'updated_at', 'deleted_at')
    list_filter = ('is_active', 'is_deleted')
    list_display_links = ['get_girisimci_full_name','girisim_adi']
    search_fields = ['girisimci__full_name', 'girisim_adi']
    inlines = [GirisimHaberleriInline, GirisimGelismelerHedeflerInline, GirisiminYatirimTurlariInline ]

    
    # ImportExport:
    resource_class = GirisimModelResource
    
    def get_girisimci_full_name(self, obj):
        return obj.girisimci.full_name
    get_girisimci_full_name.short_description = 'Girisimci Full Name'
    

admin.site.register(GirisimHaberleri, GirisimHaberleriAdmin)
admin.site.register(GirisimGelismelerHedefler, GirisimGelismelerHedeflerAdmin)
admin.site.register(GirisiminYatirimTurlari, GirisiminYatirimTurlariAdmin)
admin.site.register(Girisim, GirisimAdmin)

