from django.shortcuts import render, get_object_or_404
from .models import UserProfile
from .forms import UserProfileForm


def profile(request):
    """ Display the user's profile """

    profile = get_object_or_404(UserProfile, user=request.user)

    form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    # adding reviews later
    
    template = 'profiles/profile.html'
    context = {
        'form': form,
        'profile': profile,
        'orders': orders,
    }

    return render(request, template, context)
