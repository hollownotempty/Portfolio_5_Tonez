from django.shortcuts import redirect
from django.contrib import messages
from .forms import NewsletterForm
# Create your views here.

def newsletter_signup(request):

    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            instance = form.save()
            instance.save()
            messages.success(request, 'Thank you for signing up to the newsletter.')
    
    return redirect('home')
