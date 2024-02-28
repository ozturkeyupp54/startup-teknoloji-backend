from django.urls import path
from .views import GirisimciListView, GirisimciCreateView

urlpatterns = [
    path('girisimciler_listesi/', GirisimciListView.as_view(template_name='girisimci/girisimci_list.html'), name='girisimci_list'),
    path('create/', GirisimciCreateView.as_view(template_name='girisimci/girisimci_create.html'), name='girisimci_create'),
    # Diğer URL pattern'larını buraya ekleyebilirsiniz
]
