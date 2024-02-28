import django_filters
from django_filters import CharFilter, BooleanFilter, NumberFilter

from category.models import Category


class CategoryFilter(django_filters.FilterSet):
    title = CharFilter(field_name='name', lookup_expr='icontains')
    parent = NumberFilter(field_name='parent__id')

    is_active = BooleanFilter(field_name='is_active')
    is_deleted = BooleanFilter(field_name='is_deleted')

    class Meta:
        model = Category
        fields = []
