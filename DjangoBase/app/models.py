from django.db import models


class Product(models.Model):
    reference = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=50)
    volume = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)
