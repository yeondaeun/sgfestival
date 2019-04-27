from django.shortcuts import render, redirect, get_object_or_404
from .models import Foodtruck, Comment, Menu
from .forms import CommentForm
import random

# Create your views here.
def index(request):
    trucks = Foodtruck.objects.all
    return render(request, 'foodtruck/index.html', {'trucks_list':trucks})

def detail(request, index):
    truck = get_object_or_404(Foodtruck, pk=index)
    comments = Comment.objects.filter(foodtruck=truck)
    menus = Menu.objects.filter(foodtruck=truck)

    adv = ['신나있는', '화가 난', '호전적인', '정신을 바짝 차린', '거만한', '부끄러워하는', '당황한', '시니컬한', '광란의', '만족한', '유쾌한', '질투하는', '복수심에 불타는']
    color = ['초록', '빨간', '파란', '노란', '하얀', '금색', '보라', '네이비', '핑크', '검은', '무지개', '오트밀']
    noun = ['물소', '호랑이', '사자', '토끼', '얼룩소', '치타', '강아지', '비버', '미어캣', '수달', '종달새', '쿼카', '앵무새', '나무늘보']
    

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.writer = ""+random.choice(adv)+" "+random.choice(color)+" "+random.choice(noun)+""
            comment.foodtruck = truck
            comment.save()
            return redirect('detail', index=truck.pk)
    elif request.method == "GET":
        form = CommentForm()
        return render(request, 'foodtruck/detail.html', {'truck':truck, 'comments':comments, 'menus':menus})