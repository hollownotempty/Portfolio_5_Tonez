from django.shortcuts import get_object_or_404, render, redirect, reverse
from django.contrib import messages
from store.models import Packs

# Create your views here.


def shopping_cart(request):
    """ A view to show shopping cart. """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add items to the bag """

    product = Packs.objects.get(pk=item_id)

    quantity = 1
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        messages.warning(request, 'You already have this pack in your cart!')
    else:
        messages.success(request, f'Added {product.name} to your cart.')
        cart[item_id] = quantity

    request.session['cart'] = cart
    return redirect(redirect_url)


def remove_from_cart(request, item_id):
    """ Add items to the bag """

    product = get_object_or_404(Packs, pk=item_id)

    cart = request.session.get('cart', {})

    cart.pop(item_id)

    request.session['cart'] = cart

    messages.success(request, f'Removed {product.name} from your cart.')
    return redirect(reverse('shopping_cart'))
