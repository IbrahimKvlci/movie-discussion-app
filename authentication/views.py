from django.shortcuts import render,redirect
from django.contrib.auth import logout

from .forms import SignupForm
from .models import Profile

# Create your views here.

def logout_view(request):
    logout(request)

    return redirect('/')

def new_user(request):

    if request.method=="POST":
        form=SignupForm(request.POST,request.FILES)

        if form.is_valid():
            profile=form.save()

            return redirect('authentication:login')
    else:
        form=SignupForm()

    return render(request,'authentication/signup.html',{
        'form':form,
    })