from __future__ import unicode_literals
from django.utils import timezone
from django.db import models


# Create your models here.
class Booth(models.Model):
    name = models.CharField(max_length=200)
    place = models.CharField(max_length=200)
    content = models.TextField()
    checkbooth = models.IntegerField()

class Photo(models.Model):
    booth = models.ForeignKey(Booth, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', blank=True )
    created_at = models.DateTimeField(auto_now_add=True)

# 게시글 조회 기록 저장
class HitCount(models.Model):
   ip = models.CharField(max_length=15, default=None, null=True)  # ip 주소
   booth = models.ForeignKey(Booth, on_delete=models.CASCADE)  # 게시글
   date = models.DateField(default=timezone.now(), null=True, blank=True)  # 조회수가 올라갔던 날짜 