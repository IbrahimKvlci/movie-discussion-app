from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required 

from .models import ConversationRoom,ConversationRoomMessage
from .forms import ConversationMessageForm

from external_api.moviedb_api import moviedb

from movies.models import UserMovie
from authentication.models import Profile


# Create your views here.

@login_required
def new_conversation_room(request,movie_id):
    conversation_room=ConversationRoom()
    conversation_room.movie_id=movie_id
    conversation_room.created_by=request.user
    conversation_room.save()
    conversation_room.members.add(request.user)

    return redirect('conversationrooms:rooms',movie_id)

def rooms(request,movie_id):
    movie=moviedb.get_movie_by_id(movie_id)
    user_movie=None
    if request.user.is_authenticated:
        user_movie=UserMovie.objects.get_or_none(movie_id=movie_id,user=request.user)

    likes=UserMovie.objects.get_likes(movie_id)
    dislikes=UserMovie.objects.get_dislikes(movie_id)
    favorites=UserMovie.objects.get_favorites(movie_id)

    is_like=user_movie.is_like if user_movie else None
    is_favorite=user_movie.is_favorite if user_movie else False

    movie_rooms=ConversationRoom.objects.filter(movie_id=movie_id)

    return render(request,'conversationrooms/movieconversationrooms.html',{
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
        },
        'rooms':movie_rooms
    })

def conversation_room(request,room_pk,movie_id):
    conversation_messages=ConversationRoom.objects.get(pk=room_pk).conversation_room_messages.all()
    if request.method=="POST":
        form=ConversationMessageForm(request.POST)

        if form.is_valid():
            conversation_message=form.save(commit=False)
            conversation_message.conversation_room=ConversationRoom.objects.get(pk=room_pk)
            conversation_message.member=request.user

            conversation_message.save()
            return redirect('conversationrooms:conversation_room', movie_id=movie_id, room_pk=room_pk)
    
    else:
        form=ConversationMessageForm()


    return render(request,'conversationrooms/movieconversationroom.html',{
        'form':form,
        'conversation_messages':conversation_messages,
    })
