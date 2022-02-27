from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.


def shopping_cart(request):
    """ A view to show shopping cart. """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add items to the bag """

    quantity = 1
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        messages.warning(request, 'You already have this pack in your cart!')
    else:
        cart[item_id] = quantity

    request.session['cart'] = cart
    return redirect(redirect_url)
