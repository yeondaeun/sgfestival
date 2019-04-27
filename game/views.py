from django.shortcuts import render, redirect, get_object_or_404
from .models import Question, Answer
# Create your views here.

def game_start(request):
    return render(request, "game_start.html")


def answer_new(request):
    questions = Question.objects.all
    if request.method == 'POST':
        a1 = request.POST.get('answer_1')
        a2 = request.POST.get('answer_2')
        a3 = request.POST.get('answer_3')
        a4 = request.POST.get('answer_4')
        a5 = request.POST.get('answer_5')
        a6 = request.POST.get('answer_6')
        a7 = request.POST.get('answer_7')
        a8 = request.POST.get('answer_8')
        a9 = request.POST.get('answer_9')
        a10 = request.POST.get('answer_10')
        a11 = request.POST.get('answer_11')
        a12 = request.POST.get('answer_12')
        a13 = request.POST.get('answer_13')
        a14 = request.POST.get('answer_14')
        a15 = request.POST.get('answer_15')
        a16 = request.POST.get('answer_16')
        a17 = request.POST.get('answer_17')
        a18 = request.POST.get('answer_18')
        a19 = request.POST.get('answer_19')
        a20 = request.POST.get('answer_20')
        name = request.POST.get('name')

        answerset = [a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16, a17, a18, a19, a20]
        realanswerset = []

        for i in range(1, 21,1): 
            question =Question.objects.get(id=i)
            realanswerset.append(question.answer)
        total=0
        for i in range(20):
            if int(realanswerset[i])==int(answerset[i]): total+=1

        answer = Answer.objects.create(c1=a1, c2=a2, c3=a3, c4=a4, c5=a5, c6=a6, c7=a7, c8=a8, c9=a9, c10=a10, c11=a11, c12=a12, c13=a13,
        c14=a14, c15=a15, c16=a16, c17=a17, c18=a18, c19=a19, c20=a20, name=name, total=total)

        return redirect("game_result", pk=answer.id)
    elif request.method=='GET':
        return render(request, "game_home.html",{"questions_list":questions})


        
def answer_result(request, pk):
    answer = get_object_or_404(Answer, pk=pk)
    total = answer.total
    name = answer.name
    rangelist=[]
    for i in range(0,21):
        rangelist.append([i,0])
    for answer in Answer.objects.all():
        rangelist[answer.total][1]+=1
    rangelist = reversed(rangelist)
    return render(request, "game_result.html", {'totalpoint':total, 'result':rangelist, 'name':name})
