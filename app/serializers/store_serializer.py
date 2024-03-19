from rest_framework import serializers
from ..models.store_model import Store


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ['store_id', 'store_location']
