from django.shortcuts import render, redirect, reverse
from .models import Package
from checkout.models import Order
from django.contrib.auth.decorators import login_required


def get_packages(request):
    """ A view to show the packages """

    packages = Package.objects.all()

    context = {
        'packages': packages,
    }

    return render(request, 'packages/packages.html', context)

@login_required
def update_cart(request, package_id):
    """ A view to see updated cart """

    cart = request.session.get('cart', {})
    # package = Package.objects.get(id  = package_id)
    cart[package_id] = True
    to_return = []
    total = 0
    request.session['cart'] = cart

    for p in Package.objects.all():
        id = str(p.id)
        if id in cart and cart[id] is True:
            to_return.append(p)
            total += p.price

    context = {
        'packages': to_return,
        'total': total,
    }

    return redirect(reverse('checkout'))
