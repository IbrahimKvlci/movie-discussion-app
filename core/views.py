from django.shortcuts import render
from django.http import HttpResponse

from external_api.moviedb_api import moviedb

from movies.models import UserMovie

# Create your views here.

def index(request):
    try:
        top_movies=moviedb.get_top_movies(1)
    except:
        top_movies=[]

    top_movies_with_interactions=[{'top_movie':top_movie,'interactions':{'likes':UserMovie.objects.get_likes(top_movie['id']),'favorites':UserMovie.objects.get_favorites(top_movie['id'])}} for top_movie in top_movies]

    return render(request,'core/index.html',{
        'top_movies':top_movies_with_interactions,
    })