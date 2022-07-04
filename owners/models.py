from unicodedata import name
from django.db import models

class Owner(models.Model):
    name = models.CharField(max_length=10)
    _email = models.EmailField(max_length=254)
    age = models.IntegerField()

    class Meta:
        db_table = 'owners'

class Dog(models.Model):
    owner = models.ForeignKey('Owner', on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    age = models.IntegerField()

    class Meta:
        db_table = 'dogs'