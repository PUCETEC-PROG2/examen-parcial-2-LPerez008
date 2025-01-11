from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from .models import Movie
# Create your views here.

def index(request):
    movie = Movie.objects.order_by('title')
    template = loader.get_template('index.html')
    return HttpResponse(template.render({
        'movies': movie,
    },
    request))