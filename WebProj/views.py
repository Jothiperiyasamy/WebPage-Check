from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'home.html')

def count(request):
    mytext=request.GET['yourtext']
    yourtext=mytext.split()
    worddic={}
    for word in yourtext:
        if word in worddic:
            worddic[word] += 1
        else:
            worddic[word] = 1

    return render(request,'count.html',{'text':mytext,'worddic':worddic})

def about(request):
    return render(request,'about.html')
