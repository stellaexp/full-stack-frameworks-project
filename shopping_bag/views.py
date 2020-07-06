from django.shortcuts import render


def view_bag(request):
    """ A view to return a shoppers bag content """

    return render(request, 'shopping_bag/bag.html')
