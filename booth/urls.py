from django.urls import path, include
from booth import views

from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('boothindex/', views.booth_list, name='booth_list'),
    path('fleeindex/', views.flee_list, name='flee_list'),
    path('tuesindex/', views.tues_list, name='tues_list'),
    path('wednesindex/', views.wednes_list, name='wednes_list'),  
    path('thursindex/', views.thurs_list, name='thurs_list'),  
    path('detail/<int:index>', views.booth_detail, name='booth_detail'),
]
