from django.urls import path
from alt_reklam_alani.views import footer_reklami_olustur, track_image_view

app_name = 'alt_reklam_alani'

urlpatterns = [
    path('footer_reklami_olustur/', footer_reklami_olustur, name='advertisement/reklam_olustur'),
    path('<int:pk>/track-image-view/<str:image_field_name>/', track_image_view, name='track_image_view'),

]

