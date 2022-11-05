from distutils.command import upload
from shutil import move
from django.db import models

# Create your models here.


class Movie(models.Model):
    movie_name = models.CharField(max_length=255)
    movie_desc = models.TextField()
    movie_image = models.ImageField(upload_to="static/images/movies")

    def __str__(self):
        return self.movie_name


class Tableform(models.Model):
    movie_name = models.CharField(max_length=255)
    director = models.CharField(max_length=255)
    year = models.IntegerField()

    def __str__(self):
        return self.movie_name

class Actor(models.Model):
    actor_img=models.ImageField(upload_to="static/images/actors")
    actor_name=models.CharField(max_length=255)
    actor_desc=models.TextField()

    def __str__(self):
        return self.actor_name