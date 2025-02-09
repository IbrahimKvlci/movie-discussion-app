from django.urls import path
from django.contrib.auth import views as auth_views

from .forms import LoginForm
from . import views

app_name='authentication'

urlpatterns = [
    path('login/',auth_views.LoginView.as_view(template_name='authentication/login.html',authentication_form=LoginForm),name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('signup/',views.new_user,name='signup')
]
