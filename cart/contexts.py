from django.shortcuts import get_object_or_404
from store.models import Packs


def cart_contents(request):
    """ Context processor to access bag contents anywhere in the app """

    cart_items = []
    total = 0
    product_count = 0
    discount_percentage = 0
    cart = request.session.get('cart', {})

    

    for item_id, quantity in cart.items():
        pack = get_object_or_404(Packs, pk=item_id)
        total += pack.price
        product_count += 1
        stripe_price_id = pack.stripe_price_id
        cart_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'pack': pack,
            'stripe_price_id': stripe_price_id,
        })

    grand_total = total

    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
        'grand_total': grand_total,
        'discount': discount_percentage,
    }
    return context
