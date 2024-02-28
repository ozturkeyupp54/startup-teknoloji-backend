import django_filters
from girisim.models import Girisim

class GirisimFilter(django_filters.FilterSet):
    class Meta:
        model = Girisim
        fields = {
            'girisim_adi': ['exact', 'icontains'],
            'girisimde_calisan_sayisi': ['exact'],
            'girisim_location_city': ['exact'],
            'girisimin_bulundugu_sektor': ['exact'],
            # 'calisma_durumu': ['exact'],
            # Diğer filtreleme alanlarını ekleyebilirsiniz
        }
