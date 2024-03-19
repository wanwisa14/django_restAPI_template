from django.urls import path
from ..views.sale_view import SaleList, SaleDetailUpdateDelete, SaleDeleteAll


class SaleUrls():
    urlpatterns = [
        path('sales/', SaleList.as_view(), name='store_list'),
        path('sales/<int:store_id>/',
             SaleDetailUpdateDelete.as_view(), name='store_detail'),
        path('stores/deleteAll/', SaleDeleteAll.as_view(),
             name='store_delete_all'),
    ]
