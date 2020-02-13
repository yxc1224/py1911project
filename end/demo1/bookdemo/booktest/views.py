from django.shortcuts import render

from django.template import loader
# Create your views here.

from .models import Book,Hero

from django.http import HttpResponse

def index(request):
    # return HttpResponse("这里是首页")
    # 1.获取模板
    template=loader.get_template('index.html')
    # 2.渲染模板数据
    books=Book.objects.all()
    context={'books':books}
    result=template.render(context)
    # 3.将渲染结果返回
    return HttpResponse(result)


def about(request):
    return HttpResponse("这里是关于")

def detail(request,bookid):
    # return HttpResponse("这里是详情")
    template=loader.get_template('detail.html')
    book=Book.objects.get(id=bookid)
    context={"book":book}
    result=template.render(context)
    return HttpResponse(result)


# 使用django模板