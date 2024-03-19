from django.urls import path
from ..views.store_view import StoreList, StoreDetailUpdateDelete, StoreDeleteAll


class StoreUrls():
    urlpatterns = [
        path('stores/', StoreList.as_view(), name='store_list'),
        path('stores/<int:store_id>/',
             StoreDetailUpdateDelete.as_view(), name='store_detail'),
        path('stores/deleteAll/', StoreDeleteAll.as_view(),
             name='store_delete_all'),
    ]
