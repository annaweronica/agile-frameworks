from django.shortcuts import render
from .models import Package
from checkout.models import Order


def get_packages(request):
    """ A view to show the packages """

    packages = Package.objects.all()

    context = {
        'packages': packages,
    }

    return render(request, 'packages/packages.html', context)


def update_cart(request, package_id):
    """ A view to see updated cart """

    cart = request.session.get('cart', {})
    # package = Package.objects.get(id  = package_id)
    cart[package_id] = True

    to_return = []

    request.session['cart'] = cart

    for p in Package.objects.all():
        id = str(p.id)
        if id in cart and cart[id] == True:
            to_return.append(p)
        
    context = {
        'packages': to_return,
    }

    return render(request, 'checkout/checkout.html', context)
