"""models of products"""
from django.db import models
from django.conf import settings
import stripe

# Create your models here.
class Product ( models.Model ):
    """save products"""
    name = models.TextField( max_length=250 )
    description = models.TextField()
    amount = models.IntegerField( default=1 )
    image = models.ImageField( upload_to='products/', blank=True, null=True )

    price = models.IntegerField() # price
    currency = models.CharField( max_length=7 ) # currency
    date_added = models.DateTimeField( auto_now_add=True )

    # saves the identifier of stripe
    stripe_product_id = models.CharField( max_length=22, blank=True, null=True )
    stripe_price_id = models.CharField( max_length=22, blank=True, null=True )

    def save(self, *args, **kwargs):

        client = stripe.StripeClient( settings.STRIPE_SECRET_KEY )

        starter_subscription = client.v1.products.create(params={
            "name": self.name,
            "description": "$12/Month subscription",
        })

        starter_subscription_price = client.v1.prices.create(params={
            "unit_amount": self.price,
            "currency": "usd",
            "recurring": {"interval": "month"},
            "product": starter_subscription['id'],
        })

        # Save these identifiers
        self.stripe_price_id = starter_subscription.id
        self.stripe_product_id = starter_subscription_price.id
        print(f"Success! Here is your starter subscription product id: {starter_subscription.id}")
        print(f"Success! Here is your starter subscription price id: {starter_subscription_price.id}")

        super().save(*args, **kwargs)
