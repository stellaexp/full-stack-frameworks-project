from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your shopping basket")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51H8Lv8JY9BftfxITI4p6ea6WQicFAA51SEG2mfmejFaP28Lzosvo8WcQuUKTFBxPK8nSVoUfFG5QGUSPWRHku0R000V9mnx2YR',
        'client_secret_key': 'test client secret',
    }

    return render(request, template, context)
