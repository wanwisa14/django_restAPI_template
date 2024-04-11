from django.urls import path
from .views import StoreDetailUpdateDelete, StoreList, StoreDeleteAll, ProductDetailUpdateDelete, ProductList, ProductDeleteAll, SaleList, SaleDetailUpdateDelete, SaleDeleteAll

urlpatterns = [
    # store
    path('stores/', StoreList.as_view(), name='store_list'),
    path('stores/<int:store_id>/',
         StoreDetailUpdateDelete.as_view(), name='store_detail'),
    path('stores/deleteAll/', StoreDeleteAll.as_view(), name='store_delete_all'),
    # product
    path('products/', ProductList.as_view(), name='product_list'),
    path('products/<int:product_id>/',
         ProductDetailUpdateDelete.as_view(), name='product_detail'),
    path('products/deleteAll/',
         ProductDeleteAll.as_view(), name='product_delete_all'),
    path('sales/', SaleList.as_view(), name='sale_list'),
    path('sales/<int:transaction_id>/',
         SaleDetailUpdateDelete.as_view(), name='sale_detail'),
    path('sales/deleteAll/', SaleDeleteAll.as_view(), name='sale_delete_all'),
]
