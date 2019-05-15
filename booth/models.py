from __future__ import unicode_literals
from django.utils import timezone
from django.db import models


# Create your models here.
class Booth(models.Model):
    name = models.CharField(max_length=200)
    place = models.CharField(max_length=200)
    content = models.TextField()
    checkbooth = models.CharField(max_length=200, default='')

class Photo(models.Model):
    booth = models.ForeignKey(Booth, on_delete=models.CASCADE)
    image = models.CharField(max_length=2000, default='', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

