from django.urls import path
from .views import AuthorDetailView

app_name='author'

urlpatterns = [
    path('detail/<slug:slug>/', AuthorDetailView.as_view(), name='author_detail'),
]

