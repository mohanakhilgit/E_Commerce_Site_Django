from django.shortcuts import render
from website.models import Product  # type: ignore
from django.db.models import Q

# Create your views here.


def search_result(request):
    product = None
    query = None
    if 'q' in request.GET:
        query = request.GET.get('q')
        products = Product.objects.all().filter(Q(name__contains=query) | Q(description__contains=query))
        return render(request, 'search.html', {'query': query, 'products': products})
