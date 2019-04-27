from django.urls import path, include
from booth import views

from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', views.booth_list, name='booth_list'),
    path('detail/<int:index>', views.booth_detail, name='booth_detail'),
]
