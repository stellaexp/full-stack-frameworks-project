from django.http import HttpResponse


class stripe_webhook:
    # Handles Stripe Webhooks
    def __init__(self, request):
        self.request = request

    def handle_event(self, event):

        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        # Handles payment_intent.succeeded webhook from Stripe
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        # Handles payment_intent.payment_failed webhook from Stripe
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
