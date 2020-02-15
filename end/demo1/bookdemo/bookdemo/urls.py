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
    # path('', include('booktest.urls',namespace='booktest'))
    # 将admin和index函数绑定
    # path('index/',index),
    # path('list/',list),
    # path('jsondata/',jsondata)
    path('', include('polls.urls',namespace='polls'))
]

#  项目的所有路由地址配置文件
# 总路由配置文件


#  硬编码 在html 中有很多超级链接  其中href属性如果携程绝对路径 这种就叫做硬编码
# 在开发的过程中  可能需要反复修改路由
# 解除硬编码
# 1需要给应用一个 app_name="应用名"  下载应用的urls.py中（分路由里面）
# 2在项目路由中给应用分流时  在include中   提供命名空间
# 3在应用中给每一个路由一个名字
# 4在html中使用  href="{% url '命名空间:路由name' 实参列表 %}"
# 以前定位路由  靠总路由正则表达式+应用路由正则表达式
# 解除硬编码之后  使用  应用命名空间+应用路由名字

