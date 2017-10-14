import django_filters

from .models import Goods

class GoodsFilter(django_filters.rest_framework.FilterSet):
    name = django_filters.CharFilter(name='name',lookup_expr='icontains')
    class Meta:
        model = Goods
        fields = ['name']