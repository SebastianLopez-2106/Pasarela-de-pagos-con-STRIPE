from django.shortcuts import render

from .models import Product

# Create your views here.
def home ( request ):
    """this is the home page, in this page show all products"""

    products = Product.objects.order_by( '-date_added' )


    context = { 'products' : products }
    return render( request, "home/home.html", context )
