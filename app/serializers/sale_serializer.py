from rest_framework import serializers
from ..models.sale_model import Sale


class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = ['transaction_id', 'transaction_date', 'transaction_time', 'transaction_qty',
                  'store_id', 'store_location', 'product_id', 'unit_price',
                  'product_category', 'product_name', 'product_detail']
