from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm
from packages.models import Package


def checkout(request):

    order_form = OrderForm()
    cart = request.session.get('cart', {})
    # package = Package.objects.get(id  = package_id)

    to_return = []
    total = 0

    for p in Package.objects.all():
        id = str(p.id)
        if id in cart and cart[id] == True:
            to_return.append(p)
            total += p.price

    context = {
        'packages': to_return,
        'total': total,
        'order_form': order_form,
        'stripe_public_key': 'pk_test_OzflgG0UPSMxMSxV0zqtJwJq00A9VPyuuV',
        'client_secret': 'test client secret',
    }

    return render(request, 'checkout/checkout.html', context)
