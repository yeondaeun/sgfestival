from django.shortcuts import render, redirect, get_object_or_404
from .models import Question, Answer, Award
# Create your views here.

def game_start(request):
    return render(request, "game/game_start.html")

def game_waiting(request):
    return render(request, "game/game_waiting.html")

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
        
        i1 = request.POST.get('id_1')
        i2 = request.POST.get('id_2')
        i3 = request.POST.get('id_3')
        i4 = request.POST.get('id_4')
        i5 = request.POST.get('id_5')
        i6 = request.POST.get('id_6')
        i7 = request.POST.get('id_7')
        i8 = request.POST.get('id_8')
        i9 = request.POST.get('id_9')
        i10 = request.POST.get('id_10')
        i11 = request.POST.get('id_11')
        i12 = request.POST.get('id_12')
        i13 = request.POST.get('id_13')
        i14 = request.POST.get('id_14')
        i15 = request.POST.get('id_15')
        i16 = request.POST.get('id_16')
        i17 = request.POST.get('id_17')
        i18 = request.POST.get('id_18')
        i19 = request.POST.get('id_19')
        i20 = request.POST.get('id_20')
        answerset = {i1:a1, i2:a2, i3:a3, i4:a4, i5:a5, i6:a6, i7:a7, i8:a8, i9:a9, i10:a10, 
        i11:a11, i12:a12, i13:a13, i14:a14, i15:a15, i16:a16, i17:a17, i18:a18, i19:a19, i20:a20}
        realanswerset = {}

        # for i in range(1, 21,1): 
        #     question =Question.objects.get(id=i)
        #     realanswerset.append(question.answer)
        # for i in Question.objects.all:
        #     realanswerset[i.id]=i.answer
        for k in answerset.keys():
            question = Question.objects.get(id=k)
            realanswerset[k] = question.answer
        total=0
        # for i in range(20):
        #     if int(realanswerset[i])==int(answerset[i]): total+=1
        for k, v in answerset.items():
            if(realanswerset[k]==int(v)): total+=1
        answer = Answer.objects.create(c1=a1, c2=a2, c3=a3, c4=a4, c5=a5, c6=a6, c7=a7, c8=a8, c9=a9, c10=a10, c11=a11, c12=a12, c13=a13,
        c14=a14, c15=a15, c16=a16, c17=a17, c18=a18, c19=a19, c20=a20, name=name, total=total)

        return redirect("game_result", pk=answer.id)
    elif request.method=='GET':
        return render(request, "game/game_home.html",{"questions_list":questions})


        
def answer_result(request, pk):
    answer = get_object_or_404(Answer, pk=pk)
    count = answer.id
    total = answer.total
    name = answer.name
    rangelist=[]
    for i in range(0,21):
        rangelist.append([i,0])
    for answer in Answer.objects.all():
        rangelist[answer.total][1]+=1
    rangelist = reversed(rangelist)
    if total == 20: award = Award.objects.get(id=1)
    elif total>=15: award = Award.objects.get(id=2)
    elif total>=10: award = Award.objects.get(id=3)
    elif total>=6: award = Award.objects.get(id=4)
    else: award = Award.objects.get(id=5)
    return render(request, "game/game_result.html", {'totalpoint':total, 'result':rangelist, 'name':name, 'award':award, 'count':count})
