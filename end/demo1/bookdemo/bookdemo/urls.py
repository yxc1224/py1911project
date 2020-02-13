"""bookdemo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# 路由  每个网址均需要绑定视图函数  视图函数给与页面返回

# from django.http import HttpResponse
# def index(request):
#     return HttpResponse("这里是首页")
#
# def list(request):
#     return HttpResponse("这里是列表")
#
# def jsondata(request):
#     return HttpResponse("{'name':'yxc','age':'23'}")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('booktest/', include('booktest.urls'))
    # 将admin和index函数绑定
    # path('index/',index),
    # path('list/',list),
    # path('jsondata/',jsondata)
]

#  项目的所有路由地址配置文件
# 总路由配置文件
