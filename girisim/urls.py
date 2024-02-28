from django.urls import path
from .views import (
    GirisimListView, GirisimDetailView, girisim_create, girisim_update, girisim_delete, GirisimSearchView,
    GirisimHaberleriListView, GirisimHaberleriDetailView, girisimhaberleri_create, girisimhaberleri_update,
    girisimhaberleri_delete,
    GirisimGelismelerHedeflerListView, GirisimGelismelerHedeflerDetailView, girisimgelismelerhedefler_create,
    girisimgelismelerhedefler_update, girisimgelismelerhedefler_delete,
)

urlpatterns = [
    path('', GirisimListView.as_view(), name='girisim_list'),
    path('<int:pk>/', GirisimDetailView.as_view(), name='girisim_detail'),
    path('create/', girisim_create, name='girisim_create'),
    path('update/<int:pk>/', girisim_update, name='girisim_update'),
    path('delete/<int:pk>/', girisim_delete, name='girisim_delete'),
    path('search/', GirisimSearchView.as_view(), name='girisim_search'),

    path('girisimhaberleri/', GirisimHaberleriListView.as_view(), name='girisimhaberleri_list'),
    path('girisimhaberleri/<int:pk>/', GirisimHaberleriDetailView.as_view(), name='girisimhaberleri_detail'),
    path('girisimhaberleri/create/', girisimhaberleri_create, name='girisimhaberleri_create'),
    path('girisimhaberleri/update/<int:pk>/', girisimhaberleri_update, name='girisimhaberleri_update'),
    path('girisimhaberleri/delete/<int:pk>/', girisimhaberleri_delete, name='girisimhaberleri_delete'),

    path('girisimgelismelerhedefler/', GirisimGelismelerHedeflerListView.as_view(), name='girisimgelismelerhedefler_list'),
    path('girisimgelismelerhedefler/<int:pk>/', GirisimGelismelerHedeflerDetailView.as_view(),
         name='girisimgelismelerhedefler_detail'),
    path('girisimgelismelerhedefler/create/', girisimgelismelerhedefler_create,
         name='girisimgelismelerhedefler_create'),
    path('girisimgelismelerhedefler/update/<int:pk>/', girisimgelismelerhedefler_update,
         name='girisimgelismelerhedefler_update'),
    path('girisimgelismelerhedefler/delete/<int:pk>/', girisimgelismelerhedefler_delete,
         name='girisimgelismelerhedefler_delete'),
]
