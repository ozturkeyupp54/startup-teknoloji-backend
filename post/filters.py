import django_filters
from django_filters import CharFilter, BooleanFilter, NumberFilter

from post.models import Post


class PostFilter(django_filters.FilterSet):
    title = CharFilter(field_name='title', lookup_expr='icontains')
    creator = CharFilter(field_name='creator', lookup_expr='icontains')
    
    category = NumberFilter(field_name='category')
    category_slug = CharFilter(field_name='category__slug', lookup_expr='icontains')

    is_active = BooleanFilter(field_name='is_active')
    is_deleted = BooleanFilter(field_name='is_deleted')

    popular_post = BooleanFilter(field_name='popular_post')

    class Meta:
        model = Post
        fields = []
