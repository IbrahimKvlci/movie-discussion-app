from django.urls import path

from . import views

app_name='movies'

urlpatterns = [
    path('rooms/<int:movie_id>/like/',views.like,name='like'),
    path('rooms/<int:movie_id>/dislike/',views.dislike,name='dislike'),
    path('rooms/<int:movie_id>/favorite/',views.favorite,name='favorite')
]


