from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response

from .models import Product
from .serializers import ProductSerializer
from .utils import longest_word


class ProductListView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class SearchCoords(APIView):

    def get_queryset(self):
        products = Product.objects.all()
        product_name = self.request.query_params.get('product.name')
        if product_name:
            products_names = [product.name for product in products]
            result = longest_word(products_names, product_name)
            if result:
                return products.filter(name=result)
        return []

    def get(self, request, format=None):
        products = self.get_queryset()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)




