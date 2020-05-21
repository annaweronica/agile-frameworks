from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required


from .forms import OrderForm
from .models import Order, OrderLineItem

from packages.models import Package
from packages.views import get_packages

from profiles.forms import UserProfileForm
from profiles.models import UserProfile

import stripe


@login_required
def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    cart = request.session.get('cart', {})
    if request.method == 'POST':
        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'street_address1': request.POST['address'],
            'street_address2': request.POST['address2'],
            'town_or_city': request.POST['city'],
            # 'country': request.POST['country'],

        }

        order_form = OrderForm(form_data)

        if order_form.is_valid():
            order = order_form.save()
            for package_id, selected in cart.items():
                package = Package.objects.get(id=package_id)
                order_line_item = OrderLineItem(
                    order=order,
                    package=package,
                )
                order_line_item.save()

            request.session['save_iquantitynfo'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success',
                                    args=[order.order_number]))
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')

    order_form = OrderForm()

    # package = Package.objects.get(id  = package_id)

    to_return = []
    total = 3

    for p in Package.objects.all():
        id = str(p.id)
        if id in cart and cart[id] is True:
            to_return.append(p)
            total += p.price

    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing.')

    context = {
       'packages': to_return,
        'total': total,
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, 'checkout/checkout.html', context)
    # return redirect(reverse('checkout_success', args=[order_number]))


@login_required
def checkout_success(request, order_number):

    """ To display successful checkout """

    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        # Attach the user's profile to the order
        order.user_profile = profile
        order.save()


    # Save the user's info
    if save_info:
        profile_data = {
            'default_phone_number': order.phone_number,
            'default_town_or_city': order.town_or_city,
            'default_street_address1': order.street_address1,
            'default_street_address2': order.street_address2,
            # 'default_country': order.country,
        }
        user_profile_form = UserProfileForm(profile_data,
                                            instance=profile)
        if user_profile_form.is_valid():
            user_profile_form.save()

    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.')

    # if 'bag' in request.session:
        # del request.session['bag']

    """Send the user a confirmation email"""
    cust_email = order.email
    subject = render_to_string(
        'checkout/confirmation_emails/confirmation_email_subject.txt',
        {'order': order})
    body = render_to_string(
        'checkout/confirmation_emails/confirmation_email_body.txt',
        {'order': order, 'contact_email': settings.DEFAULT_FROM_EMAIL})

    send_mail(
        subject,
        body,
        settings.DEFAULT_FROM_EMAIL,
        [cust_email]
    )

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
