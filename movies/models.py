from pyexpat import model
from turtle import title
from django.db import models

class Actor(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    date_of_birth = models.DateField()

    class Meta:
        db_table = 'actors'
    
    def __str__(self):
        return self.first_name, self.last_name

class Movie(models.Model):
    title = models.CharField(max_length=50)
    release_date = models.DateField()
    running_time = models.IntegerField()
    add_to_actor = models.ManyToManyField(Actor)

    class Meta:
        db_table = 'movies'
    
    def __str__(self):
        return self.title

class Actor_movie(models.Model):
    actor = models.ForeignKey('Actor', on_delete=models.CASCADE)
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE)

    class Meta:
        db_table = 'actor_movie'