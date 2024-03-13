from django.urls import path
from .views import StoreDetailUpdateDelete, StoreList

urlpatterns = [
    path('stores/', StoreList.as_view(), name='store_list'),
    path('stores/<int:store_id>/',
         StoreDetailUpdateDelete.as_view(), name='store_detail'),
]
