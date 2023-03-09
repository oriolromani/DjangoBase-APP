from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIRequestFactory
from rest_framework import status

from .views import ProductListView
from .utils import longest_word


class ProductViewTests(TestCase):
    def test_create_product(self):
        """
        Assess we can create a new product
        """
        factory = APIRequestFactory()
        view = ProductListView.as_view()
        data = {
            "reference": "randomreference",
            "name": "test product",
            "volume": 123.4,
        }
        url = reverse("products")
        request = factory.post(url, data=data, format="json")
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_list_of_products(self):
        """
        Test we can get a list of existing products
        """
        factory = APIRequestFactory()
        view = ProductListView.as_view()
        url = reverse("products")
        request = factory.get(url, format="json")
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TestUtils(TestCase):
    def test_given_example(self):
        letters = ['mercury', 'venus', 'earth', 'mars', 'jupiter', 'saturn', 'uranus', 'neptune']
        word = 'ajsxuytcnhre'
        self.assertEqual(longest_word(letters, word), 'saturn')
