from django.contrib import admin
from alt_reklam_alani.models import FooterReklami



class FooterReklamiAdmin(admin.ModelAdmin):
    list_display = ('get_kampanya_creator_full_name', 'kampanya_basligi', 'sirket_adi', 'kampanya_baslangic_tarihi', 'is_active', 'created_at' ,'updated_at')
    list_filter = ('is_active', 'is_deleted')
    search_fields = ['kampanya_creator__full_name', 'kampanya_basligi', 'sirket_adi', 'kampanya_baslangic_tarihi']

    def get_kampanya_creator_full_name(self, obj):
        return obj.kampanya_creator.full_name

    get_kampanya_creator_full_name.short_description = 'Kampanya Creator Full Name'


admin.site.register(FooterReklami, FooterReklamiAdmin)

# Register your models here.
