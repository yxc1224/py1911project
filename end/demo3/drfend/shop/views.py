from rest_framework import viewsets
from .models import *
from .serializers import *
from django.http import HttpResponse, JsonResponse

# Create your views here.

# 通过api_view装饰器  可以将基于函数的视图转换成 APIView基于类视图
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_object_or_404

from django.views import View


class CategoryListView(View):
    """
    继承Django自带的View类需要重写对应的http方法
    """

    def get(self, request):
        return HttpResponse("返回列表成功")

    def post(self, request):
        return HttpResponse("创建成功")


class CategoryDetailView(View):
    def get(self, request, cid):
        return HttpResponse("返回单个对象")

    def put(self, request, cid):
        return HttpResponse("修改成功put")

    def patch(self, request, cid):
        return HttpResponse("修改成功patch")

    def delete(self, request, cid):
        return HttpResponse("删除成功")


@api_view(['GET', 'POST'])
def categoryList(request):
    if request.method == "GET":
        print("获取到GET请求参数", request.query_params)

        # instance 为需要序列化的对象，来源于数据库
        queryset = Category.objects.all()
        seria = CategorySerializer(instance=queryset, many=True)
        print(seria.data)
        return Response(seria.data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        # data 为序列化对象  来源于从请求中提取的数据
        queryset = request.data
        seria = CategorySerializer(data=queryset)
        # 从请求中提取的数据 序列化之前需要进行校验
        if seria.is_valid():
            seria.save()
            return Response(seria.data, status=status.HTTP_201_CREATED)
        else:
            return Response(seria.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def categoryDetail(request, cid):
    model = get_object_or_404(Category, pk=cid)
    if request.method == "GET":
        seria = CategorySerializer(model)
        return Response(seria.data, status=status.HTTP_200_OK)
    elif request.method == "PUT" or request.method == "PATCH":
        #  从请求中提取参数  替换掉从数据库中取出的数据
        seria = CategorySerializer(instance=model, data=request.data)
        if seria.is_valid():
            seria.save()
            return Response(seria.data, status.HTTP_200_OK)
        else:
            return Response(seria.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        model.delete()
        return Response(status.HTTP_204_NO_CONTENT)
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
