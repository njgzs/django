from rest_framework import serializers
from .models import Goods,GoodsCategory
# GoodsCategory
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields ="__all__"
        
class GoodsSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Goods
        fields ="__all__"
        
        
class GoodsCategorySerializer(serializers.ModelSerializer):
    sub_cat = CategorySerializer(many=True)
    class Meta:
        model = GoodsCategory
        fields ="__all__"
                