from django.shortcuts import render
from .models import Package


def get_packages(request):
    """ A view to show the packages """

    packages = Package.objects.all()

    context = {
        'packages': packages,
    }

    return render(request, 'packages/packages.html', context)
