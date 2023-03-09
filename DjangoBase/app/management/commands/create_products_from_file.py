import json
from django.core.management.base import BaseCommand, CommandError

from app.models import Product


class Command(BaseCommand):
    help = 'upload products from file'

    def add_arguments(self, parser):
        parser.add_argument('filepath')

    def handle(self, *args, **options):
        filepath = options['filepath']

        with open(filepath) as json_file:
            data = json.load(json_file)
            for product in data['products']:
                try:
                    Product.objects.create(
                        reference=product['reference'],
                        name=product['name'],
                        volume=product['volume'],
                    )
                    print("Product %s created" % product["reference"])
                except Exception as e:
                    print(e)



