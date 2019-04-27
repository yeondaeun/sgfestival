from django.contrib import admin
from .models import Foodtruck, Menu, Comment
# Register your models here.

admin.site.register(Foodtruck)
admin.site.register(Menu)
admin.site.register(Comment)