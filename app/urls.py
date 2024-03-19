from django.urls import path
from .routing.product_urls import ProductUrls
from .routing.sale_urls import SaleUrls
from .routing.store_urls import StoreUrls


urlpatterns = []
urlpatterns.extend(ProductUrls.urlpatterns)
urlpatterns.extend(SaleUrls.urlpatterns)
urlpatterns.extend(StoreUrls.urlpatterns)
