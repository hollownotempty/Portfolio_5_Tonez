from django.http import HttpResponse



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
            content=f'Webhook Received: {event["type"]}',
            status=200
        )

    def handle_checkout_session_completed(self,event):
        """
        Handle the payment_intent_succeeded webhook event
        """

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
