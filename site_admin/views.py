from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError
from .forms import AddProductForm
from contact.forms import ReplyForm
from store.models import Packs
from contact.models import ContactSubmission

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


def remove_product(request):
    """
    Returns the remove product menu
    """
    packs = Packs.objects.all()
    context = {
        'packs': packs,
    }
    return render(request, 'site_admin/remove_product.html', context)


def delete_product(request, product_id):
    """
    Deletes product from database
    """
    product = Packs.objects.get(pk=product_id)
    product.delete()
    messages.success(request, 'Successfully deleted product!')
    return redirect('remove_product')


def update_product(request):
    """
    Returns the update item menu
    """
    packs = Packs.objects.all()
    context = {
        'packs': packs,
    }
    return render(request, 'site_admin/update_product.html', context)


def update_product_detail(request, product_id):
    """
    Returns the individual page to update an item
    """
    product = Packs.objects.get(pk=product_id)
    form = AddProductForm(request.POST or None, instance=product)

    if form.is_valid():
        form.save()
        messages.success(request, f'Successfully updated {product.name}.')
        return redirect('update_product')

    context = {
        'product': product,
        'form': form,
    }
    return render(request, 'site_admin/update_product_detail.html', context)


def contact_submissions(request):
    submissions = ContactSubmission.objects.all()

    context = {
        'submissions': submissions,
    }
    return render(request, 'site_admin/contact_submissions.html', context)


def contact_submission_detail(request, submission_id):
    """
    Details of contact submission and reply form
    """
    submission = ContactSubmission.objects.get(pk=submission_id)
    form = ReplyForm()

    if request.method == 'POST':
        form = ReplyForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.submission = submission
            instance.save()
            submission.responded_to = True
            submission.save()

    context ={
        'submission': submission,
        'form': form,
    }
    return render(request, 'site_admin/contact_submission_detail.html', context)
