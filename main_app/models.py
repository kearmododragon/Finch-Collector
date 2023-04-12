from django.db import models

# Create your models here.

class Game(models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    franchise = models.CharField(max_length=100)
    description =  models.TextField(max_length=250)
    #owned = models.BooleanField(CheckboxInput)
def __str__(self):
    return self.name