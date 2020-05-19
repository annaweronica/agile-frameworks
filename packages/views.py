from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from .models import Package
from checkout.models import Order
from django.contrib.auth.decorators import login_required

from .forms import PackageForm


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


def get_package_management(request):
    """ A view to display a package management to
        meet CRUD requirement """
    return render(request, 'packages/package_management.html')


def add_package(request):
    """ Add a package to the offer """
    if request.method == 'POST':
        form = PackageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added package')
            return redirect(reverse('add_package'))
        else:
            messages.error(request,
                           'Failed to add a package. Please ensure the form is correct')
    else:
        form = PackageForm()

    template = 'packages/add_package.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def edit_package(request, package_id):
    """ Edit a package in the offer """

    package = get_object_or_404(Package, pk=package_id)
    if request.method == 'POST':
        form = PackageForm(request.POST, request.FILES, instance=package)
        if form.is_valid():
            form.save()
            messages.success(request, 'The package successfully updated!')
            return redirect(reverse('package_id', args=[product.id])) # it was product_detail 
        else:
            messages.error(request, 'Failed to update a package. Please ensure the form is valid.')
    else:
        form = PackageForm(instance=package)
        messages.info(request, f'You are editing {package.name}')

    template = 'packages/edit_package.html'
    context = {
        'form': form,
        'package': package,
    }

    return render(request, template, context)
