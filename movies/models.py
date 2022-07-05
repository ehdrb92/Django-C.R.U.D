from pyexpat import model
from turtle import title
from django.db import models

class Actor(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    date_of_birth = models.DateField()

    class Meta:
        db_table = 'actors'

class Movie(models.Model):
    title = models.CharField(max_length=50)
    release_date = models.DateField()
    running_time = models.IntegerField()

    class Meta:
        db_table = 'movies'

class Actor_movie(models.Model):
    actor = models.ForeignKey('Actor', on_delete=models.CASCADE)
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE)

    class Meta:
        db_table = 'actor_movie'