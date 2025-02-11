from django import forms

from .models import ConversationRoomMessage
class ConversationMessageForm(forms.ModelForm):
    class Meta:
        model=ConversationRoomMessage
        fields=('content',)
        widgets={
            'content':forms.TextInput(attrs={
                'class':'w-full py-4 px-6 rounded-xl border'
            })
        }

