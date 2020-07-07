from django.shortcuts import render, redirect


def view_bag(request):
    """ A view to return a shoppers bag content """

    return render(request, 'shopping_basket/bag.html')


def add_to_basket(request, item_id):
    """ Lets user add quantity of products to their shopping bag """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    request.session['bag'] = bag

    return redirect(redirect_url)
