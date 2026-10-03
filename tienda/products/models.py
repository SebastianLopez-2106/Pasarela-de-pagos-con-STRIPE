"""models of products"""
from django.db import models

# Create your models here.
class Product (models.Model):
    """save products"""
    nombre = models.TextField(max_length=250)
    description = models.TextField()

    # saves the identifier of stripe
    stripe_product_id = models.CharField(max_length=22)


class Price (models.Model):
    """price of the products"""
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='price')

    importe = models.IntegerField() # price
    currency = models.CharField(max_length=7) # currency

    stripe_price_id = models.CharField(max_length=22)


class Images (models.Model):
    """images of products"""
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')

    image = models.ImageField(upload_to='products/', blank=True, null=True)
