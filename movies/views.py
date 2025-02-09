from django.shortcuts import render,redirect

from external_api.moviedb_api import moviedb

from .models import UserMovie

# Create your views here.

def detail(request,movie_id):
    movie=moviedb.get_movie_by_id(movie_id)
    user_movie=UserMovie.objects.get(movie_id=movie_id,user=request.user)

    likes=UserMovie.objects.filter(is_like=True).count()
    dislikes=UserMovie.objects.filter(is_like=False).count()
    favorites=UserMovie.objects.filter(is_favorite=True).count()

    is_like=user_movie.is_like if user_movie else None
    is_favorite=user_movie.is_favorite if user_movie else False

    return render(request,'movies/moviedetail.html',{
        'movie':movie,
        'movie_interactions':
        {
            'likes':likes,
            'dislikes':dislikes,
            'favorites':favorites
        },
        'user_interactions':{
            'is_like':is_like,
            'is_favorite':is_favorite,
        }
    })

def like(request,movie_id):
    user_movie, created = UserMovie.objects.get_or_create(movie_id=movie_id, user=request.user)
    if user_movie.is_like:
        user_movie.is_like = None
    else:
        user_movie.is_like=True
    user_movie.save()


    return redirect('movies:detail',movie_id)

def dislike(request,movie_id):
    user_movie, created = UserMovie.objects.get_or_create(movie_id=movie_id, user=request.user)
    if user_movie.is_like==False:
        user_movie.is_like = None
    else:
        user_movie.is_like=False
    user_movie.save()


    return redirect('movies:detail',movie_id)

def favorite(request,movie_id):
    user_movie, created = UserMovie.objects.get_or_create(movie_id=movie_id, user=request.user)
    if user_movie.is_favorite:
        user_movie.is_favorite=False
    else:
        user_movie.is_favorite=True
    user_movie.save()
    
    return redirect('movies:detail',movie_id)