from rest_framework import generics, response, status
from ..models.product_model import Product
from ..serializers.product_serializer import ProductSerializer


class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'product_id'


class ProductDeleteAll(generics.DestroyAPIView):
    def delete(self, request, *args, **kwargs):
        # Delete all Product objects
        Product.objects.all().delete()
        return response.Response(status=status.HTTP_204_NO_CONTENT)
