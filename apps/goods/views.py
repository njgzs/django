from rest_framework.generics import ListAPIView 
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets,mixins
from rest_framework import filters
from rest_framework.authentication import TokenAuthentication
from django_filters.rest_framework import DjangoFilterBackend


from .models import Goods,GoodsCategory
from .serializers import GoodsSerializer,GoodsCategorySerializer
from .filters  import GoodsFilter

class GoodsPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'ps'
    page_query_param = 'p'
    max_page_size = 100

class GoodsListViewSet(mixins.ListModelMixin,viewsets.GenericViewSet):
    """
    商品列表页 分页 搜索 过滤 排序
    """
    authentication_classes = (TokenAuthentication,)
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    pagination_class = GoodsPagination
    filter_backends = (DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter)
    filter_class = GoodsFilter
    search_fields = ('name','goods_brief','goods_desc')
    ordering_fields = ('name','shop_price')
    
class CategoryViewSet(mixins.ListModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet):
    '''
    商品分类列表
    '''
    queryset = GoodsCategory.objects.filter(category_type=1)
    serializer_class = GoodsCategorySerializer