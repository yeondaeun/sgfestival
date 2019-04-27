from django.db import models

# Create your models here
class Foodtruck(models.Model):
    truckname = models.CharField(max_length=200)
    truckplace = models.CharField(max_length=200)
    truckphoto = models.ImageField(upload_to='images/', blank=True)
    truckinfo = models.TextField()
    truckdate = models.CharField(max_length=200)
    trucktime = models.CharField(max_length=200)

class Menu(models.Model):
    foodtruck = models.ForeignKey(Foodtruck, on_delete=models.CASCADE)
    menuname = models.CharField(max_length=200)
    menuprice = models.CharField(max_length=200)

class Comment(models.Model):
    foodtruck = models.ForeignKey(Foodtruck, on_delete=models.CASCADE)
    writer = models.CharField(max_length=200)
    content = models.TextField()
