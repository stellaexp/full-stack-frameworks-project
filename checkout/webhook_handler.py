from django.http import HttpResponse
from .models import CustomerOrder, OrderItem
from products.models import Product
import json
import time


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
        intent = event.data.object
        pid = intent.id
        bag = intent.metadata.bag
        save_info = intent.metadata.save_info

        billing_details = intent.charges.data[0].billing_details
        shipping_details = intent.shipping
        grand_total = round(intent.charges.data[0].amount / 100, 2)

        # Clean data in shipping details
        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None

                order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                order = CustomerOrder.objects.get(
                    full_name__iexact=shipping_details.name,
                    email__iexact=billing_details.email,
                    telephone__iexact=shipping_details.phone,
                    postcode__iexact=shipping_details.address.postal_code,
                    county__iexact=shipping_details.address.city,
                    country__iexact=shipping_details.address.country,
                    address1__iexact=shipping_details.address.line1,
                    address2__iexact=shipping_details.address.line2,
                    grand_total=grand_total,
                    original_bag=bag,
                    stripe_pid=pid,
                )
                order_exists = True
                break
            except CustomerOrder.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if order_exists:
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS',
                status=200)
        else:
            order = None
            try:
                order = CustomerOrder.objects.create(
                    full_name=shipping_details.name,
                    email=billing_details.email,
                    telephone=shipping_details.phone,
                    postcode=shipping_details.address.postal_code,
                    county=shipping_details.address.city,
                    country=shipping_details.address.country,
                    address1=shipping_details.address.line1,
                    address2=shipping_details.address.line2,
                    original_bag=bag,
                    stripe_pid=pid,
                )
                for item_id, item_data in json.loads(bag).items():
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_item = OrderItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        order_item.save()
                    else:
                        for quantity in item_data.items():
                            order_item = OrderItem(
                                order=order,
                                product=product,
                                quantity=quantity,
                            )
                            order_item.save()
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500)
        return HttpResponse(
            content=f'Webhook received: {event["type"]} | SUCCESS',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        # Handles payment_intent.payment_failed webhook from Stripe
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
