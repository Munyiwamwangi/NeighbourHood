import datetime as dt
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from.models import Neighborhood, Neighbor, Post, Business

# Create your views here.


def about(request):
    return render(request, "about.html")

def nyumbani(request):
    images = Neighborhood.objects.all()
    return render(request, 'neighborhood.html', {"images": images})
