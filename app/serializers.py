from rest_framework import serializers
from .models import Store, Product, Sale


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ['store_id', 'store_location']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['product_id', 'product_name']

class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = ['transaction_id', 'transaction_date', 'transaction_time', 'transaction_qty', 'store_id', 'product_id', 'unit_price', 'product_category', 'product_name', 'product_detail']