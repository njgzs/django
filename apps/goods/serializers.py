from rest_framework import serializers
from .models import Goods,GoodsCategory
# GoodsCategory
class GoodsCategorySerializer(serializers.ModelSerializer):
    # parent_category=self()
    class Meta:
        model = GoodsCategory
        fields ="__all__"
        
class GoodsSerializer(serializers.ModelSerializer):
    category = GoodsCategorySerializer()
    class Meta:
        model = Goods
        fields ="__all__"