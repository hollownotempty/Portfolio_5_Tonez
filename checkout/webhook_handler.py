from django.http import HttpResponse
from checkout.models import Order, OrderLineItem
from store.models import Packs
from .forms import OrderForm

import json



class StripeWhHandler:
    """
    Custom webhook handler
    """
    def __init__(self, request):
        self.request = request

    def handle_event(self,event):
        """
        Handle a generic/unknown/unexpected webhook event
        """

        return HttpResponse(
            content=f'walalalalala: {event["type"]}',
            status=200
        )

    def handle_checkout_session_completed(self,event):
        """
        Handle the payment_intent_succeeded webhook event
        """

        md = event.data.object.metadata
        cart = event.data.object.metadata.cart

        print(cart)

        form_data = {
            'full_name': md.full_name,
            'email': md.email,
            'phone_number': md.phone_number,
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

        return HttpResponse(
            content=f'Session Checkout Webhook received: {event["type"]}',
            status=200
        )

    def handle_payment_intent_payment_failed(self,event):
        """
        Handle the payment_intent_failed webhook event
        """

        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200
        )
