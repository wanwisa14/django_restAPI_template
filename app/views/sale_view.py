from rest_framework import generics, response, status
from ..models.sale_model import Sale
from ..serializers.sale_serializer import SaleSerializer


class SaleList(generics.ListCreateAPIView):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer


class SaleDetailUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
    lookup_field = 'Sale_id'


class SaleDeleteAll(generics.DestroyAPIView):
    def delete(self, request, *args, **kwargs):
        # Delete all Sale objects
        Sale.objects.all().delete()
        return response.Response(status=status.HTTP_204_NO_CONTENT)
