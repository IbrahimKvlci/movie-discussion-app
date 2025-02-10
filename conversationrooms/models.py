from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ConversationRoom(models.Model):
    movie_id=models.IntegerField()
    members=models.ManyToManyField(User,related_name='joined_conversation_rooms')
    created_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='created_conversation_rooms')
    created_at=models.DateField(auto_now_add=True)
    modified_at=models.DateField(auto_now=True)

    class Meta:
        ordering=('-modified_at',)

class ConversationRoomMessage(models.Model):
    conversation_room=models.ForeignKey(ConversationRoom,on_delete=models.CASCADE,related_name='conversation_room_messages')
    member=models.ForeignKey(User,on_delete=models.CASCADE,related_name='sent_conversation_room_messages')
    content=models.TextField(max_length=300)
    created_at=models.DateField(auto_now_add=True)