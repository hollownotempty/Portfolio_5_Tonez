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
stripe.api_version = "2020-08-27"

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
    if request.method == 'POST':
        cart = request.session.get('cart', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
        }

        # order_form = OrderForm(form_data)
        # if order_form.is_valid():
        #     order = order_form.save(commit=False)
        #     order.save()
        #     for item_id, item_data in cart.items():
        #         product = Packs.objects.get(id=item_id)
        #         if isinstance(item_data, int):
        #             order_line_item = OrderLineItem(
        #                 order=order,
        #                 product=product,
        #             )
        #             order_line_item.save()

    YOUR_DOMAIN = 'http://localhost:8000/'

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

    # request.session['order_number'] = order.order_number

    return redirect(checkout_session.url, code=303)


def cancel(request):

    return redirect(reverse('shopping_cart'))


def success(request):

    if 'cart' in request.session:
        del request.session['cart']

    return render(request, 'checkout/success.html')
