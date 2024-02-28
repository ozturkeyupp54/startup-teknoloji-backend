from django.urls import path
from post.views import PostDetailView


app_name = 'post'

urlpatterns = [
    path('detail/<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
    # other URL patterns...
]