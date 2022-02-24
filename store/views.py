from django.shortcuts import render

# Create your views here.


def packs(request):
    # Return packs page

    return render(request, 'store/packs.html')
