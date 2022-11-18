from django.db import models

# Create your models here.
class Place(models.Model):
    name = models.CharField(max_length=250)
    img = models.ImageField(upload_to='photos')
    desc = models.TextField()

class Team(models.Model):
    name = models.CharField(max_length=250)
    img1 = models.ImageField(upload_to='photos')
    brief = models.TextField()