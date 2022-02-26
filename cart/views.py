from django.shortcuts import render, redirect

# Create your views here.

def shopping_cart(request):
    """ A view to show shopping cart. """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add items to the bag """

    quantity = 1
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    # if item_id in list(bag.keys()):
    #     # do something
    # else:
    #     bag[item_id] = quantity

    cart[item_id] = quantity

    request.session['cart'] = cart
    print(request.session['cart'])
    return redirect(redirect_url)
