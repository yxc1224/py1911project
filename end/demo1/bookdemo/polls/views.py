from django.shortcuts import render, redirect, reverse
from django.template import loader
from django.http import HttpResponse
from .models import Polls, Pollsmsg,User
from django.views.generic import View, TemplateView, ListView
from django.contrib.auth import authenticate, login as lin, logout as lot


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
    polls_text = Polls.objects.get(id=pollsid)
    if request.method == "GET":
        print("当前用户",request.user.username)
        if request.user and request.user.username !="":
            print(request.user.pollss.all(),"11",polls_text)

            if polls_text in request.user.pollss.all():

                url = reverse("polls:ballot", args=(polls_text.id,))
                return redirect(to=url)
            else:
                return render(request, 'addpolls.html', {"polls": polls_text})
        else:
            url = reverse("polls:ballot", args=(polls_text.id,))
            return redirect(to=url)
    elif request.method == "POST":
        pol1 = request.POST.get("pol")
        pollsmsg = Pollsmsg.objects.get(id=pol1)
        pollsmsg.coutmsg += 1
        pollsmsg.save()
        url = reverse("polls:ballot", args=(polls_text.id,))
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


def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        #  可以使用Django自带的用户认证   认证成功返回用户  失败返回none
        user = authenticate(username=username, password=password)
        if user:
            # 调用Django的登录方法  生成cookie
            lin(request, user)
            url=reverse("polls:polls")
            return redirect(to=url)
        else:
            url=reverse("polls:login")
            return redirect(to=url)



def regist(request):
    if request.method == "GET":
        return render(request, 'regist.html')
    elif request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        password2=request.POST.get("password2")
        if User.objects.filter(username=username).count()>0:
            return HttpResponse("用户名已存在")
        else:
            if password==password2:
                User.objects.create_user(username=username,password=password)
                url=reverse("polls:login")
                return redirect(to=url)
            else:
                return HttpResponse("两次密码不一致")

def logout(request):
    #  调用Django的登出方法  为了删除cookie
    lot(request)
    url=reverse("polls:polls")
    return redirect(to=url)