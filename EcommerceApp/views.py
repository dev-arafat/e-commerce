from django.shortcuts import render, redirect
from .models import *


def index(request):
    slider = Slide.objects.all()
    Hedar = hedar.objects.all()
    Newsletter = newsletter.objects.all()
    NewArrivals = newArrivals.objects.all()
    NewArrivalsSecond = newArrivalsSecond.objects.all()
    Trending = trending.objects.all()
    TrendingSecond = trendingSecond.objects.all()
    topRated = TopRated.objects.all()
    topRatedSecond = TopRatedSecond.objects.all()
    NewProducts = newProducts.objects.all()
    return render(request, 'index.html', locals())
