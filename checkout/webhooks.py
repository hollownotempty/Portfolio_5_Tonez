import json
from django.http import HttpResponse
from django.conf import settings
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from checkout.webhook_handler import StripeWhHandler

import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY

# Using Django
@require_POST
@csrf_exempt
def webhook(request):
    payload = request.body
    event = None

    try:
        event = stripe.Event.construct_from(
        json.loads(payload), stripe.api_key
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)

    handler = StripeWhHandler(request)

    event_map = {
        'checkout.session.completed': handler.handle_checkout_session_completed,
        'payment_intent.payment_failed': handler.handle_payment_intent_payment_failed,
    }

    event_type = event['type']

    event_handler = event_map.get(event_type, handler.handle_event)
    
    response = event_handler(event)
    return response