from rest_framework import viewsets
from .models import *
from .serializers import *
from django.http import HttpResponse, JsonResponse

# Create your views here.

# 通过api_view装饰器  可以将基于函数的视图转换成 APIView基于类视图
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET', 'POST'])
def categoryList(request):
    print(request, type(request))
    if request.method == "GET":
        print("获取到GET请求参数", request.query_params)
        return HttpResponse("获取列表成功")
    elif request.method == "POST":
        print("获取到POST请求参数", request.data)
        return HttpResponse("创建成功")

@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def categoryDetail(request, cid):
    if request.method == "GET":
        print("获取到GET请求参数", request.query_params)
        return HttpResponse("获取单个成功")
    elif request.method == "PUT" or request.method == "PATCH":
        print("获取到PUT/PATCH请求参数", request.data)
        return HttpResponse("修改成功")
    elif request.method == "DELETE":
        return HttpResponse("删除成功")
    else:
        return HttpResponse('当前路由不允许' + request.method + '操作')


class CategoryViewSets(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class GoodViewSets(viewsets.ModelViewSet):
    queryset = Good.objects.all()
    serializer_class = GoodSerializer


class GoodImgsViewSets(viewsets.ModelViewSet):
    queryset = GoodImgs.objects.all()
    serializer_class = GoodImgsSerializer
