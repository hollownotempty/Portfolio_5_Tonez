from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm

# Create your views here.


def contact_page(request):
    """ Returns the contact form page """
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            instance = form.save()
            instance.save()
            messages.success(request, 'Contact request submitted successfully.')
            return redirect('contact')


    context = {
        'form': form,
    }
    return render(request, 'contact/contact.html', context)
