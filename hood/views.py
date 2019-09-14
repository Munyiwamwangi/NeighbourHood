import datetime as dt
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from.models import Neighboorhood, People, Post, Business

# Create your views here.


def about(request):
    return render(request, "about.html")

def nyumbani(request):
    images = Neighboorhood.objects.all()
    return render(request, 'neighborhood.html', {"images": images})


def search_results(request):

    if 'neighboorhood' in request.GET and request.GET["neighboorhood"]:
        search_term = request.GET.get("neighboorhood")
        searched_neighboorhoods = Neighboorhood.search_by_hood_name(
            search_term)
        message = f"{search_term}"

        return render(request, 'all-news/search.html', {"message": message, "neighboorhood": searched_neighboorhoods})

    else:
        message = "You haven't searched for any neighboorhood"
        return render(request, 'search.html', {"message": message})

