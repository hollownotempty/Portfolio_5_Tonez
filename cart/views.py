from django.shortcuts import render

# Create your views here.

def shopping_cart(request):
    """ A view to show shopping cart. """

    return render(request, 'cart/cart.html')