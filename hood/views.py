from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from .models import Neighboorhood, Comment, Post, Business
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

# Create your views here.


def about(request):
    return render(request, "hood/about.html")

def home(request):
    images = Neighboorhood.objects.all()
    return render(request, 'hood/neighborhood.html', {"images": images})

def blogging(request):

    context={
    'posts':Post.objects.all()
    }

    return render(request, 'hood/home.html', context)




def search_results(request):

    if 'neighboorhood' in request.GET and request.GET["neighboorhood"]:
        search_term = request.GET.get("neighboorhood")
        searched_neighboorhoods = Neighboorhood.search_by_hood_name(
            search_term)
        message = f"{search_term}"

        return render(request, 'hood/search.html', {"message": message, "neighboorhood": searched_neighboorhoods})

    else:
        message = "You haven't searched for any neighboorhood"
        return render(request, 'hood/search.html', {"message": message})

