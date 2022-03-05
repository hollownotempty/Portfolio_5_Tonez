from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings

import stripe

from store.models import Packs



from .forms import OrderForm

stripe.api_key = settings.STRIPE_SECRET_KEY

# Create your views here.


def checkout(request):
    """ renders checkout template """
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There's nothing in your cart!")
        return redirect(reverse('packs'))
    
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
    }

    return render (request, template, context)


def create_checkout_session(request):
    """ Create checkout session Stripe """

    YOUR_DOMAIN = 'https://8000-hollownotempty-portfolio-kuwz79nvo6k.ws-eu34.gitpod.io/'

    cart = request.session.get('cart', {})

    line_items = []

    for item_id, quantity in cart.items():
        pack = get_object_or_404(Packs, pk=item_id)
        stripe_price_id = pack.stripe_price_id
        pd = {
            'price': stripe_price_id,
            'quantity': quantity,
        }
        
        line_items.append(pd)

    checkout_session = stripe.checkout.Session.create(
        line_items=line_items,
        mode='payment',
        success_url=YOUR_DOMAIN + 'checkout/success/',
        cancel_url=YOUR_DOMAIN + 'checkout/cancel/',
    )

    return redirect(checkout_session.url, code=303)


def success(request):
    return render(request, 'checkout/success.html')


def cancel(request):
    return render(request, 'checkout/cancel.html')
