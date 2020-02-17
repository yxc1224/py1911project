from django.shortcuts import render, redirect, reverse

from django.template import loader

from .models import Polls,Pollsmsg

from django.http import HttpResponse


# Create your views here.

def polls(request):

    pollss = Polls.objects.all()
    return render(request, 'polls.html', {"pollss": pollss})



def addpolls(request, pollsid):
    polls=Polls.objects.get(id=pollsid)
    if request.method == "GET":
        return render(request, 'addpolls.html', {"polls": polls})
    elif request.method == "POST":
        pol1=request.POST.get("pol")
        pollsmsg=Pollsmsg.objects.get(id=pol1)
        pollsmsg.coutmsg+=1
        pollsmsg.save()
        url = reverse("polls:ballot",args=(polls.id,))
        return redirect(to=url)

def ballot(request,pollsid):
    polls = Polls.objects.get(id=pollsid)
    return render(request, 'ballot.html', {"polls": polls})

