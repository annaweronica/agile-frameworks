from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


# @login_required()
def checkout(request):
    checkout = request.session.get('checkout', {})
    # if not checkout:
    #    messages.error(request, "You have no selected packages")
    #    return redirect(reverse('get_packages'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
    }

    return render(request, template, context)
