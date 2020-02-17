from django.shortcuts import render, redirect, reverse

from django.template import loader

from django.http import HttpResponse
from .models import Polls, Pollsmsg

from django.views.generic import View, TemplateView, ListView


# Create your views here.

def polls(request):
    pollss = Polls.objects.all()
    return render(request, 'polls.html', {"pollss": pollss})


class IndexView(ListView):
    # 方法二、继承ListView
    # template_name指明使用的模板
    template_name = "polls.html"
    # queryset 指明返回的结果列表
    queryset = Polls.objects.all()
    # context_object_name 指明返回字典参数的健
    context_object_name = "pollss"

    # 方法一、继承的TemplateView
    # template_name = "polls/index.html"
    # def get_context_data(self, **kwargs):
    #     return {"questions":Question.objects.all()}


def addpolls(request, pollsid):
    polls = Polls.objects.get(id=pollsid)
    if request.method == "GET":
        return render(request, 'addpolls.html', {"polls": polls})
    elif request.method == "POST":
        pol1 = request.POST.get("pol")
        pollsmsg = Pollsmsg.objects.get(id=pol1)
        pollsmsg.coutmsg += 1
        pollsmsg.save()
        url = reverse("polls:ballot", args=(polls.id,))
        return redirect(to=url)


class Detailview(View):

    def get(self, request, pollsid):
        polls = Polls.objects.get(id=pollsid)
        return render(request, 'addpolls.html', {"polls": polls})

    def post(self, request, pollsid):
        polls = Polls.objects.get(id=pollsid)
        pol1 = request.POST.get("pol")
        pollsmsg = Pollsmsg.objects.get(id=pol1)
        pollsmsg.coutmsg += 1
        pollsmsg.save()
        url = reverse("polls:ballot", args=(polls.id,))
        return redirect(to=url)


def ballot(request, pollsid):
    polls = Polls.objects.get(id=pollsid)
    return render(request, 'ballot.html', {"polls": polls})


class ResultView(View):
    def get(self, request, pollsid):
        polls = Polls.objects.get(id=pollsid)
        return render(request, 'ballot.html', {"polls": polls})
