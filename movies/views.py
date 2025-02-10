from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required 

from django.contrib import messages

from external_api.moviedb_api import moviedb

from .models import UserMovie

# Create your views here.

# def detail(request,movie_id):
#     movie=moviedb.get_movie_by_id(movie_id)
#     user_movie=None
#     if request.user.is_authenticated:
#         user_movie=UserMovie.objects.get_or_none(movie_id=movie_id,user=request.user)

#     likes=UserMovie.objects.get_likes(movie_id)
#     dislikes=UserMovie.objects.get_dislikes(movie_id)
#     favorites=UserMovie.objects.get_favorites(movie_id)

#     is_like=user_movie.is_like if user_movie else None
#     is_favorite=user_movie.is_favorite if user_movie else False

#     return render(request,'conversationrooms/movieconversationrooms.html',{
#         'movie':movie,
#         'movie_interactions':
#         {
#             'likes':likes,
#             'dislikes':dislikes,
#             'favorites':favorites
#         },
#         'user_interactions':{
#             'is_like':is_like,
#             'is_favorite':is_favorite,
#         }
#     })

@login_required
def like(request,movie_id):
    user_movie, created = UserMovie.objects.get_or_create(movie_id=movie_id, user=request.user)
    if user_movie.is_like:
        user_movie.is_like = None
    else:
        user_movie.is_like=True
    user_movie.save()


    return redirect('conversationrooms:rooms',movie_id)

@login_required
def dislike(request,movie_id):
    user_movie, created = UserMovie.objects.get_or_create(movie_id=movie_id, user=request.user)
    if user_movie.is_like==False:
        user_movie.is_like = None
    else:
        user_movie.is_like=False
    user_movie.save()


    return redirect('conversationrooms:rooms',movie_id)

@login_required
def favorite(request,movie_id):
    user_movie, created = UserMovie.objects.get_or_create(movie_id=movie_id, user=request.user)
    if user_movie.is_favorite:
        user_movie.is_favorite=False
    else:
        user_movie.is_favorite=True
    user_movie.save()
    
    return redirect('conversationrooms:rooms',movie_id)
