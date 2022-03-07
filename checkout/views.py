from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import json
import stripe

from store.models import Packs
from .models import Order, OrderLineItem


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


def cancel(request):
    return redirect(reverse('shopping_cart'))



def success(request):

    if 'cart' in request.session:
        del request.session['cart']

    return render(request, 'checkout/success.html')


@csrf_exempt
def stripe_webhook(request):
    """ Webhook handler from stripe docs """
    payload = request.body
    event = None

    try:
        event = stripe.Event.construct_from(
            json.loads(payload), stripe.api_key
        )
    except ValueError as e:
    # Invalid payload
        return HttpResponse(status=400)

    # Handle the event
    if event.type == 'payment_intent.succeeded':
        payment_intent = event.data.object # contains a stripe.PaymentIntent
        print('PaymentIntent was successful!')
    elif event.type == 'payment_method.attached':
        payment_method = event.data.object # contains a stripe.PaymentMethod
        print('PaymentMethod was attached to a Customer!')
    # ... handle other event types
    else:
        print('Unhandled event type {}'.format(event.type))

    return HttpResponse(status=200)
