from django.contrib import admin

# Register your models here.
from .models import Photo, Booth, HitCount



admin.site.register(Photo)

admin.site.register(Booth)
admin.site.register(HitCount)
