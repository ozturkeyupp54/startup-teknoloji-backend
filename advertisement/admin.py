from django.contrib import admin
from unidecode import unidecode  # Import the unidecode library
from advertisement.models import Advertisement


class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ('get_kampanya_creator_full_name', 'kampanya_basligi', 'sirket_adi', 'kampanya_baslangic_tarihi', 'is_active', 'created_at' ,'updated_at')
    list_filter = ('is_active', 'is_deleted')
    search_fields = ['kampanya_creator__full_name', 'kampanya_basligi', 'sirket_adi', 'kampanya_baslangic_tarihi']

    def get_kampanya_creator_full_name(self, obj):
        return obj.kampanya_creator.full_name

    get_kampanya_creator_full_name.short_description = 'Kampanya Creator Full Name'

    # Override the default search function
    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super().get_search_results(request, queryset, search_term)

        # Normalize the search term using unidecode
        search_term = unidecode(search_term)

        # Perform case-insensitive search
        queryset |= self.model.objects.filter(kampanya_creator__full_name__icontains=search_term)
        queryset |= self.model.objects.filter(kampanya_basligi__icontains=search_term)
        queryset |= self.model.objects.filter(sirket_adi__icontains=search_term)
        queryset |= self.model.objects.filter(kampanya_baslangic_tarihi__icontains=search_term)

        return queryset, use_distinct

admin.site.register(Advertisement, AdvertisementAdmin)
