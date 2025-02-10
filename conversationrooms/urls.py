from django.urls import path

from . import views

app_name='conversationrooms'

urlpatterns = [
    path('<int:movie_id>/',views.rooms,name='rooms'),
    path('<int:movie_id>/new',views.new_conversation_room,name='new')
]
