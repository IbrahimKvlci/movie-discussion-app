from django.urls import path

from . import views

app_name='movies'

urlpatterns = [
    path('detail/<int:movie_id>/',views.detail,name='detail'),
    path('detail/<int:movie_id>/like/',views.like,name='like'),
    path('detail/<int:movie_id>/dislike/',views.dislike,name='dislike'),
    path('detail/<int:movie_id>/favorite/',views.favorite,name='favorite')
]


