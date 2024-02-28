from django.urls import path
# from anket.views import create_form_view

from . import views

urlpatterns = [
    # Anket URLs
    # path('createForm/', create_form_view, name='create_form'),
    path('anketler/', views.AnketListView.as_view(template_name = 'anket/anket_list.html'), name='anket_list'),
    path('anket/<int:pk>/', views.AnketDetailView.as_view(template_name = 'anket/anket_detail.html'), name='anket_detail'),
    path('anket_create/', views.AnketCreateView.as_view(template_name = 'anket/anket_create.html'), name='anket_create'),
    path('anket_update/<int:pk>/', views.AnketUpdateView.as_view(template_name = 'anket/anket_update.html'), name='anket_update'),
    path('anket_delete/<int:pk>/', views.AnketDeleteView.as_view(), name='anket_delete'),

    # Soru URLs (nested under Anket)
    path('anket/<int:anket_pk>/sorular/', views.SoruListView.as_view(), name='soru_list'),
    path('anket/<int:anket_pk>/soru_create/', views.SoruCreateView.as_view(), name='soru_create'),
    path('soru/<int:pk>/update/', views.SoruUpdateView.as_view(), name='soru_update'),
    path('soru/<int:pk>/delete/', views.SoruDeleteView.as_view(), name='soru_delete'),

    # Cevap URLs (nested under Soru)
    path('soru/<int:soru_pk>/cevaplar/', views.CevapListView.as_view(), name='cevap_list'),

    # Sonuc URLs (nested under Anket)
    path('anket/<int:anket_pk>/sonuclar/', views.SonucListView.as_view(), name='sonuc_list'),
]

# from django.urls import path
# from anket.views import anket_olustur, soru_ekle

# urlpatterns = [
#     path('anket-olustur/', anket_olustur, name='anket_olustur'),
#     path('soru-ekle/<int:anket_id>/', soru_ekle, name='soru_ekle'),
#     # Diğer URL'leri buraya ekleyin...
# ]

# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.index, name='questionnaire_index'),
#     path('<int:questionnaire_id>/', views.questionnaire_detail, name='questionnaire_detail'),
#     path('calculate/', views.calculate, name='questionnaire_calculate'),
#     path('answer/<int:questionnaire_pk>/', views.answerpage, name='questionnaire_answer'),
# ]