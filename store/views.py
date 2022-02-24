from django.shortcuts import render, get_object_or_404
from .models import Packs
# Create your views here.


def packs(request):
    # Return packs page

    packs = Packs.objects.all()

    context = {
        'packs': packs,
    }

    return render(request, 'store/packs.html', context)

def pack_detail(request, pack_id):
    """ A view to show individual product details """

    pack = get_object_or_404(Packs, pk=pack_id)

    context = {
        'pack': pack,
    }

    return render(request, 'store/pack_detail.html', context)