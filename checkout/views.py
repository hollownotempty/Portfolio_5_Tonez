import json

from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives


import stripe

from checkout.models import OrderLineItem
from store.models import Packs
from profiles.models import UserProfile
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
        request.session['full_name'] = request.POST['full_name']
        request.session['email'] = request.POST['email']
        request.session['phone_number'] = request.POST['phone_number']

    YOUR_DOMAIN = settings.DOMAIN

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
        allow_promotion_codes=True,
        success_url=YOUR_DOMAIN + 'checkout/success/',
        cancel_url=YOUR_DOMAIN + 'checkout/cancel/',
    )

    # request.session['order_number'] = order.order_number

    return redirect(checkout_session.url, code=303)


def cancel(request):

    return redirect(reverse('shopping_cart'))


def success(request):
    """
    View to return the success page after a purchase has gone through
    """
    cart = json.dumps(request.session.get('cart', {}))

    form_data = {
            'full_name': request.session['full_name'],
            'email': request.session['email'],
            'phone_number': request.session['phone_number'],
        }

    order_form = OrderForm(form_data)

    if order_form.is_valid():
            order = order_form.save(commit=False)
            order.save()
            for item_id, item_data in json.loads(cart).items():
                    product = Packs.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                        )
                        order_line_item.save()

    if request.user.is_anonymous:
        order.user_profile = None
    else:
        profile = UserProfile.objects.get(user=request.user)
        order.user_profile = profile
        order.save()



    context = {
        'order': order,
    }

    # Email

    subject, from_email, to = f"Order: {order.order_number}", settings.EMAIL_HOST_USER, order.email
    text_content = get_template('checkout/email/checkout_success.txt').render(context)
    html_content = get_template('checkout/email/checkout_success.html').render(context)
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()

    if 'cart' in request.session:
        del request.session['cart']

    del request.session['full_name'], request.session['email'], request.session['phone_number']

    messages.success(request, "Order successfully processed!")

    return render(request, 'checkout/success.html', context)
