from django.shortcuts import render, get_object_or_404
from .models import Listings
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choices import food_choices
from django.db.models import Q


# Create your views here.
def index(request):
    listings = Listings.objects.all()

    paginator = Paginator(listings, 3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings': paged_listings
    }
    return render(request, 'listing/listing.html', context)


def search(request):
    queryset_list = Listings.objects.order_by('-list_date')

    if 'q' in request.GET:
        q = request.GET['q']
        if q:
            queryset_list = queryset_list.filter(title__icontains=q)

    context = {
        'food_choices': food_choices,
        'listings': queryset_list

    }

    return render(request, 'listing/search.html', context)
