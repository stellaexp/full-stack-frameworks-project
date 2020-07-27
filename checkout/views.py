from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings
from .forms import OrderForm
from .models import CustomerOrder, OrderItem
from products.models import Product
from shopping_basket.contexts import bag_contents

import stripe


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        bag = request.session.get('bag', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'telephone': request.POST['telephone'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'address1': request.POST['address1'],
            'address2': request.POST['address2'],
            'address3': request.POST['address3'],
            'county': request.POST['county'],
        }

        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save()
            for item_id, item_data in bag.items():
                try:
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
                except Product.DoesNotExist:
                    messages.error(request, "We can't find your item in our database.")
                    order.delete()
                    return redirect(reverse('view_bag'))

            request.session['save_info'] = 'save-info' in request.POST

            return redirect(reverse('checkout_success',
                            args=[order.order_number]))
        else:
            messages.error(request, 'There was an error with your form.')

    else:
        bag = request.session.get('bag', {})
        if not bag:
            messages.error(request, "There's nothing in your basket")
            return redirect(reverse('products'))

        current_basket = bag_contents(request)
        total = current_basket['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

    order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')

    template ='checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret_key': intent.client_secret,
    }

    return render(request, template, context)


def checkout_success(request, order_number):
    """ For successful checkouts """
    save_info = request.session.get('save_info')
    order = get_object_or_404(CustomerOrder, order_number=order_number)
    messages.success(request, f'Order successfully processed! \
        Your order is {order_number}. A confirmation \
        email will be sent to {order.email}. shortly')

    if 'bag' in request.session:
        del request.session['bag']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }
