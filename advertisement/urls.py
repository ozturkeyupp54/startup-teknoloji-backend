from django.urls import path
from advertisement.views import reklam_olustur, track_image_view, reklam_paneli, hesap_ayarlari, odemeler, fatura, bakiye

app_name = 'advertisement'

urlpatterns = [
    path('reklam_olustur/', reklam_olustur, name='advertisement/reklam_olustur'),
    path('<int:pk>/track-image-view/<str:image_field_name>/', track_image_view, name='track_image_view'),
    
    
    path('reklam_paneli/', reklam_paneli, name='advertisement/reklam_paneli'),
    path('hesap_ayarlari/', hesap_ayarlari, name='advertisement/hesap_ayarlari'),
    path('odemeler/', odemeler, name='advertisement/odemeler'),
    path('fatura/', fatura, name='advertisement/fatura'),
    path('bakiye/', bakiye, name='advertisement/bakiye'),    
    
    # Add other paths as needed...
]

