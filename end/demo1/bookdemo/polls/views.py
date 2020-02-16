from django.shortcuts import render, redirect, reverse

from django.template import loader

from .models import Polls,Pollsmsg

from django.http import HttpResponse


# Create your views here.

def polls(request):
    # return HttpResponse("这里是首页")
    # 1.获取模板
    template = loader.get_template('polls.html')
    # 2.渲染模板数据
    pollss = Polls.objects.all()
    context = {'pollss': pollss}
    result = template.render(context)
    # 3.将渲染结果返回
    return HttpResponse(result)



def addpolls(request, pollsid):
    polls=Polls.objects.get(id=pollsid)
    if request.method == "GET":
        return render(request, 'addpolls.html', {"polls": polls})
    elif request.method == "POST":
        pol1=request.POST.get("pol")

        url = reverse("polls:ballot",args=(polls.id,))
        return redirect(to=url)

def ballot(request,pollsid):
    polls = Polls.objects.get(id=pollsid)
    return render(request, 'ballot.html', {"polls": polls})

