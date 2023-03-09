from django.urls import path

from .views import ProductListView, SearchCoords

urlpatterns = [
    path('products/', ProductListView.as_view(), name='products'),
    path('shearchcoords/<str:product_name>', SearchCoords.as_view(), name='search'),
]
