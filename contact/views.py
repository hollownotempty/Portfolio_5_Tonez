from django.shortcuts import render
from .forms import ContactForm

# Create your views here.


def contact_page(request):
    """ Returns the contact form page """
    form = ContactForm()

    context = {
        'form': form,
    }
    return render(request, 'contact/contact.html', context)
