from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.contrib.auth.models import User

from .models import Profile

class LoginForm(AuthenticationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Your username',
        'class':'w-full py-4 px-6 rounded-xl'
    }))

    password=forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Password',
        'class':'w-full py-4 px-6 rounded-xl'
    }))



class SignupForm(UserCreationForm):

    first_name=forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'First Name',
        'class':'w-full py-4 px-6 rounded-xl'
    }))
    last_name=forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Last Name',
        'class':'w-full py-4 px-6 rounded-xl'
    }))
    username=forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Your username',
        'class':'w-full py-4 px-6 rounded-xl'
    }))
    email=forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder':'Email address',
        'class':'w-full py-4 px-6 rounded-xl'
    }))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Password',
        'class':'w-full py-4 px-6 rounded-xl'
    }),label='Password')
    password2=forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Repeat password',
        'class':'w-full py-4 px-6 rounded-xl'
    }),label='Repeat password')
    profile_image=forms.ImageField(required=False,widget=forms.FileInput(attrs={
        'class':'w-full py-4 px-6 rounded-xl bg-gray-300 hover:bg-gray-500 cursor-pointer'
    }))


    def save(self,commit=True):
        user=super(SignupForm,self).save(commit=False)
        user.first_name=self.cleaned_data.get('first_name')
        user.last_name=self.cleaned_data.get('last_name')
        user.email=self.cleaned_data.get('email')
        user.save()
        profile=Profile.objects.create(user=user,profile_image=self.cleaned_data.get('profile_image'))

        if(commit):
            profile.save()
        return profile
    