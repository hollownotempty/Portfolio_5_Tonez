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
        cart_items.append({
            'item_id': item_id,
            'pack': pack,
        })

    if total >= 45:
        quotient = 3 / 20
        discount_percentage = quotient * float(total)
        new_total = float(total) - discount_percentage

    grand_total = new_total

    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
        'grand_total': grand_total,
        'discount': discount_percentage,
    }
    return context
