from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User

# Create your models here.

class UserMovieManager(models.Manager):
    def get_or_none(self,**kwargs):
        try:
            return self.get(**kwargs)
        except ObjectDoesNotExist:
            return None
        
    def get_likes(self,movie_id):
        return self.filter(is_like=True,movie_id=movie_id).count()
    def get_dislikes(self,movie_id):
        return self.filter(is_like=False,movie_id=movie_id).count()
    def get_favorites(self,movie_id):
        return self.filter(is_favorite=True,movie_id=movie_id).count()


class UserMovie(models.Model):
    movie_id=models.IntegerField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    is_like=models.BooleanField(null=True)
    is_favorite=models.BooleanField(default=False)

    objects=UserMovieManager()


    
    