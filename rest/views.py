from django.shortcuts import render
from listings.choices import food_choices
from listings.models import Listings


# Create your views here.
def index(request):
    listings = Listings.objects.order_by('-list_date').filter(is_published=True)[:3]

    context = {
        'listings': listings
    }

    return render(request, 'pages/index.html', context)


def food(request):
    listings = Listings.objects.all()

    context = {
        'listings': listings
    }
    return render(request, 'pages/food.html', context)


def login(request):
    return render(request, 'pages/login.html')


def signin(request):
    return render(request, 'pages/sign-in.html')
