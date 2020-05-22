from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ContactForm
from django.core.mail import send_mail


def get_main_page(request):
    """ A view to return the main page """
    return render(request, 'agile_app/main_page.html')


def get_contact_page(request):
    """ A view to return contact page """
    name = ''
    email = ''
    comment = ''

    if request.method == 'POST':
        form = ContactForm(request.POST)
        print(form)

        if form.is_valid():
            name = form.cleaned_data.get("name")
            email = form.cleaned_data.get("email")
            comment = form.cleaned_data.get("comment")

            if request.user.is_authenticated:
                subject = str(request.user) + "'s Comment"
            else:
                form = ContactForm()
                subject = "A Visitor's Comment"

            comment = name + " with the email, " + email +\
                ", sent the following message:\n\n" + comment
            send_mail(subject, comment, email, ['anna.w.janiak@gmail.com'])

        context = {'form': form}
        print(comment)
        return render(request, 'agile_app/contact.html', context)

    else:
        form = ContactForm()
        context = {'form': form}
        return render(request, 'agile_app/contact.html', context)
