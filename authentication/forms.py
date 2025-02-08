from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class LoginForm(AuthenticationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Your username',
        'class':'w-full py-4 px-6 rounded-xl'
    }))

    password=forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Password',
        'class':'w-full py-4 px-6 rounded-xl'
    }))



class SignupForm(forms.Form):
    first_name=forms.CharField(label="First Name",max_length=100)
    last_name=forms.CharField(label="Last Name",max_length=100)
    username=forms.CharField(label='Username',max_length=100)
    email=forms.EmailField(label="Email address")
    password1=forms.CharField(widget=forms.PasswordInput)
    password2=forms.CharField(widget=forms.PasswordInput)
    profile_image=forms.ImageField(required=False)
    