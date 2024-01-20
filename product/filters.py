import django_filters
from django_filters.rest_framework import FilterSet
from .models import Product

class ProductFilter(FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    price_lt = django_filters.NumberFilter(field_name='price',lookup_expr='lte')
    price_gt = django_filters.NumberFilter(field_name='price',lookup_expr='gte')
    class Meta:
        model = Product
        fields = ['name','price_lt','price_gt']
