from django.shortcuts import render, redirect


def view_bag(request):
    """ A view to return a shoppers bag content """

    return render(request, 'shopping_basket/bag.html')


def add_to_basket(request, item_id):
    """ Lets user add quantity of products to their shopping basket """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    request.session['bag'] = bag

    return redirect(redirect_url)


def edit_basket(request, item_id):
    """ Lets user update quantity in their shopping basket """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] = quantity

    request.session['bag'] = bag

    return redirect(redirect_url)


def delete_item_from_basket(request, item_id):
    """ View to delete item from users shopping basket """

    # Looked up how to delete item from basket here
    # https://stackoverflow.com/questions/52477268/how-to-remove-an-item-from-django-session

    bag = request.session.get('bag', {})
    del bag[item_id]
    request.session['bag'] = bag

    redirect_url = request.POST.get('redirect_url')

    return redirect(redirect_url)
