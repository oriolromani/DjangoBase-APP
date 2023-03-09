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

    def get(self, request, product_name):
        products = Product.objects.all()
        products_names = [product.name for product in products]
        result = longest_word(products_names, product_name)
        print(result)
        if result:
            product = products.first()
            serializer = ProductSerializer(product)
            return Response(serializer.data)
        else:
            return Response(status='404')
