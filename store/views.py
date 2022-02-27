from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.db.models import Q
from .models import Packs
# Create your views here.


def packs(request):
    # Return packs page
    packs = Packs.objects.all()
    query = None
    category = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category']
            packs = packs.filter(category__name=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Please enter a search!")
                return redirect(reverse('packs'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            packs = packs.filter(queries)
            
    context = {
        'packs': packs,
        'search_term': query,
    }

    return render(request, 'store/packs.html', context)

def pack_detail(request, pack_id):
    """ A view to show individual product details """

    pack = get_object_or_404(Packs, pk=pack_id)

    context = {
        'pack': pack,
    }

    return render(request, 'store/pack_detail.html', context)