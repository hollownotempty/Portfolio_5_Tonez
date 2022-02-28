from django.shortcuts import render

# Create your views here.


def contact_page(request):
    """ Returns the contact form page """

    return render(request, 'contact/contact.html')
