from rest_framework.generics import ListAPIView 
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets
# Create your views here.
from .models import Goods
from .serializers import GoodsSerializer

class GoodsPagination(PageNumberPagination):
    page_size = 10;
    page_size_query_param = 'page_size'
    page_query_param = 'p'
    max_page_size = 100

class GoodsListViewSet(viewsets.GenericViewSet):
    """
    这里可以写接口描述信息
    """
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    pagination_class = GoodsPagination