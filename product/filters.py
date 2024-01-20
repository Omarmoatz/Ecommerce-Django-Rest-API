import django_filters
from django_filters.rest_framework import FilterSet
from .models import Product

class ProductFilter(FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Product
        fields = ['name','price']
