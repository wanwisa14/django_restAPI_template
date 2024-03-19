from django.urls import path
from ..views.product_view import ProductList, ProductDetailUpdateDelete, ProductDeleteAll


class ProductUrls():
    urlpatterns = [
        path('products/', ProductList.as_view(), name='product_list'),
        path('products/<int:product_id>/',
             ProductDetailUpdateDelete.as_view(), name='product_detail'),
        path('products/deleteAll/',
             ProductDeleteAll.as_view(), name='product_delete_all'),
    ]
