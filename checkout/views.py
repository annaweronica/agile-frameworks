from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


#@login_required()
def checkout(request):
    #checkout = request.session.get('checkout', {})
    # if not checkout:
    #    messages.error(request, "You have no selected packages")
    #    return redirect(reverse('get_packages'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    # user profile app
    #current_user = UserProfile.objects.filter(id = request.user.id)
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_OzflgG0UPSMxMSxV0zqtJwJq00A9VPyuuV',
        'client_secret': 'test client secret',
        # 'user': current_user,

    }

    return render(request, template)
    # return render(request, template, context)
