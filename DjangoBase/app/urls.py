from django.urls import path

from .views import ProductListView, SearchCoords

urlpatterns = [
    path('products/', ProductListView.as_view(), name='products'),
    path('shearchcoords/', SearchCoords.as_view(), name='search'),
]
