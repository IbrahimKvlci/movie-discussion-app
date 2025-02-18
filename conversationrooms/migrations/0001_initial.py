# Generated by Django 5.1.6 on 2025-02-10 15:09

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ConversationRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_id', models.IntegerField()),
                ('created_at', models.DateField(auto_now_add=True)),
                ('modified_at', models.DateField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_conversation_rooms', to=settings.AUTH_USER_MODEL)),
                ('members', models.ManyToManyField(related_name='joined_conversation_rooms', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-modified_at',),
            },
        ),
        migrations.CreateModel(
            name='ConversationRoomMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=300)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('conversation_room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='conversation_room_messages', to='conversationrooms.conversationroom')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_conversation_room_messages', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
