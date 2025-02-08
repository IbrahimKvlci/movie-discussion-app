from django.shortcuts import render
from django.http import HttpResponse

from external_api.moviedb_api import moviedb

# Create your views here.

def index(request):
    try:
        top_movies=moviedb.get_top_movies(1)
    except:
        top_movies=[]

    return render(request,'core/index.html',{
        'top_movies':top_movies,
    })