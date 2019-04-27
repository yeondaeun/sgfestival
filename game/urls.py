
from django.urls import path, include
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('answer_new/',views.answer_new, name = "answer_new"),
    path('result/<pk>/', views.answer_result, name="game_result"),
    path('start',views.game_start, name="game_start")
]
