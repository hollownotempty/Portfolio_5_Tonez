from multiprocessing import context
from re import template
from django.shortcuts import render, get_object_or_404

from checkout.models import Order

from .models import UserProfile

# Create your views here.

def profile_page(request):
    """
    Display the currently logged in user's profile
    """
    profile = get_object_or_404(UserProfile, user=request.user)
    orders = profile.orders.all()
    template = 'profiles/profile.html'
    context = {
        'profile': profile,
        'orders': orders,
    }

    return render(request, template, context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    template = 'checkout/success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)