from django.shortcuts import render


# Create your views here.
def get_main_page(request):
    """ A view to return the main page """
    return render(request, 'agile_app/main_page.html')