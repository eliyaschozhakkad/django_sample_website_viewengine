from django.shortcuts import render
from django.http import HttpResponse
from .models import Actor, Movie,Tableform

# Create your views here.


def index(request):
    listof={
        "films":Tableform.objects.all()
    }
    return render(request, "index.html",listof)


def new_release(request): 
    movies_new= {
        "movies": Movie.objects.all()
    }
    return render(request, "newmovies.html",movies_new)


def actors(request):  
    actors={
        "actor":Actor.objects.all()
    }
    return render(request, "actors.html",actors)
