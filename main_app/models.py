from django.db import models
from django.urls import reverse

# Create your models here.

class Game(models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    #notion for (B)reakfast (L)unch (D)inner to be used here
    franchise = models.CharField(max_length=100)
    #notion for (B)reakfast (L)unch (D)inner to be used here
    description =  models.TextField(max_length=250)
    

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('detail', kwargs={'game_id': self.id})
    
class levels(models.Model):
    number = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)    

    def __str__(self):
        return self.name


class Console(models.Model):
    name = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    Generation = models.CharField(max_length=100)
    description =  models.TextField(max_length=250)