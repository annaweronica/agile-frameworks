from django.shortcuts import render



# Create your views here.
def get_main_page(request):
    """ A view to return the main page """
    return render(request, 'agile_app/main_page.html')


def get_contact_page(request):
    """ A view to return the main page """
    return render(request, 'agile_app/contact.html')


def get_package_management(request):
    """ A view to display a package management to
        meet CRUD requirement """
    return render(request, 'agile_app/package_management.html')
