from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_image=models.ImageField(upload_to='profile_images/',blank=True,null=True)
    