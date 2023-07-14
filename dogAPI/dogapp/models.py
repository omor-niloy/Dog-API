from django import forms
from django.db import models
from . import options
# Create your models here.

class Breed(models.Model):
    name = models.CharField(max_length=100)
    size = models.CharField(max_length=40, choices=options.SIZE_OPTIONS)
    friendliness = models.IntegerField(choices=options.OPTIONS_1_TO_5);
    trainability = models.IntegerField(choices=options.OPTIONS_1_TO_5);
    sheddingamount = models.IntegerField(choices=options.OPTIONS_1_TO_5);
    exerciseneeds = models.IntegerField(choices=options.OPTIONS_1_TO_5);

    def __str__(self):
        return self.name

class Dog(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE)
    gender = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    favoritefood = models.CharField(max_length=100)
    favoritetoy = models.CharField(max_length=30) 

    def __str__(self):
        return self.name
