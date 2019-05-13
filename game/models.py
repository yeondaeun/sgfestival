from django.db import models
from django.utils import timezone
from django.db import models
# Create your models here.

class Question(models.Model):
    question = models.CharField(max_length=200)
    c1 = models.CharField(max_length=300)
    c2 = models.CharField(max_length=300)
    c3 = models.CharField(max_length=300)
    c4 = models.CharField(max_length=300)
    answer = models.IntegerField()
    imagelink = models.CharField(max_length=2000, default='', blank=True, null=True)

class Answer(models.Model):
    name = models.CharField(max_length=50)
    c1 = models.IntegerField(default=0)
    c2 = models.IntegerField(default=0)
    c3 = models.IntegerField(default=0)
    c4 = models.IntegerField(default=0)
    c5 = models.IntegerField(default=0)
    c6 = models.IntegerField(default=0)
    c7 = models.IntegerField(default=0)
    c8 = models.IntegerField(default=0)
    c9 = models.IntegerField(default=0)
    c10 = models.IntegerField(default=0)
    c11 = models.IntegerField(default=0)
    c12 = models.IntegerField(default=0)
    c13 = models.IntegerField(default=0)
    c14 = models.IntegerField(default=0)
    c15 = models.IntegerField(default=0)
    c16 = models.IntegerField(default=0)
    c17 = models.IntegerField(default=0)
    c18 = models.IntegerField(default=0)
    c19 = models.IntegerField(default=0)
    c20 = models.IntegerField(default=0)
    total = models.IntegerField(default=0)

class Award(models.Model):
    title = models.CharField(max_length=200, default='')
    content = models.CharField(max_length=1000)
    imagelink = models.CharField(max_length=2000, default='', blank=True, null=True)
