from django.shortcuts import render


# Create your views here.
def view_bag(request):
    """ A view display a purchase bag """
    return render(request, 'bag/bag.html')


def get_contact_page(request):
    """ A view to return the main page """
    return render(request, 'agile_app/contact_page.html')
