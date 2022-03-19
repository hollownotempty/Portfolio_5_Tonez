from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import AddProductForm

# Create your views here.

def site_admin(request):
    """
    Return the custom site admin page for superusers
    """
    return render(request, 'site_admin/site_admin.html')


def add_product(request):
    """
    Renders page and form to add new products to the database
    """
    form = AddProductForm()

    if request.method == 'POST':
        form = AddProductForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save()
            instance.save()
            messages.success(request, 'New product added successfully.')
            return redirect('add_product')

    context = {
        'form': form,
    }

    return render(request, 'site_admin/add_product.html', context)
