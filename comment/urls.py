from django.urls import path
from comment.views import create_comment

app_name = 'comment'

urlpatterns = [
    path('create/<int:post_id>/', create_comment, name='comment_create'),
    # Diğer URL pattern'larını ekleyebilirsiniz.
]
