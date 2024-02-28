from django.urls import path
from category.views import CategoryDetailView

urlpatterns = [
    # path('list/', CategoryListView.as_view(), name='category_list'),
    path('detail/<slug:slug>/', CategoryDetailView.as_view(), name='category_detail'),
]
