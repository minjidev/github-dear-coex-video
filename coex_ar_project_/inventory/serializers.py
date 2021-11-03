# serializers.py
from rest_framework import serializers

from .models import Inventory, Product, ProductType, Store, UserAction

# Make one Serializer per each ViewSet that we have in views.py
class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = ("product", "units_available", "arrival_date")
        depth = 1

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("id", "product_name", "store", "product_type", "sale_price", "image_url")

class ProductTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductType
        fields = ("__all__")

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ("__all__")


class UserActionSerializer(serializers.ModelSerializer):
    class Meta: 
        model = UserAction
        fields = ("product", "store", "action_type", "user", "date_time")

class UserActionRankingSerializer(serializers.ModelSerializer):
    ranking_points = serializers.IntegerField()
 
    class Meta: 
        model = UserAction
        fields = ["product", "ranking_points"]