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
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins


class CategoryListView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryListView2(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    # def get_queryset(self):
    #     return Category.objects.all()

    # def get_serializer_class(self):
    #     return CategorySerializer

    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class CategoryListView1(APIView):
    """
    1.继承Django自带的View类需要重写对应的http方法
    2.继承ORF自带的APIView类即可完成请求响应的封装
    """

    def get(self, request):
        seria = CategorySerializer(instance=Category.objects.all(), many=True)
        return Response(seria.data, status=status.HTTP_200_OK)

    def post(self, request):
        seria = CategorySerializer(data=request.data, many=True)
        if seria.is_valid():
            seria.save()
            return Response(seria.data, status=status.HTTP_201_CREATED)
        else:
            return Response(seria.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailView2(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                          mixins.DestroyModelMixin):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get(self, request, pk):
        return self.retrieve(request, pk)

    def put(self, request, pk):
        return self.update(request, pk)

    def patch(self, request, pk):
        return self.update(request, pk)

    def delete(self, request, pk):
        return self.delete(request, pk)


class CategoryDetailView1(APIView):
    def get(self, request, cid):
        seria = CategorySerializer(instance=get_object_or_404(Category, pk=cid))
        return Response(seria.data, status=status.HTTP_200_OK)

    def put(self, request, cid):
        seria = CategorySerializer(instance=get_object_or_404(Category, pk=cid), data=request.data)
        if seria.is_valid():
            seria.save()
            return Response(seria.data, status.HTTP_200_OK)
        else:
            return Response(seria.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, cid):
        seria = CategorySerializer(instance=get_object_or_404(Category, pk=cid), data=request.data)
        if seria.is_valid():
            seria.save()
            return Response(seria.data, status.HTTP_200_OK)
        else:
            return Response(seria.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, cid):
        get_object_or_404(Category, pk=cid).detele()
        return Response(status=status.HTTP_204_NO_CONTENT)


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


class CategoryViewSets2(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer



class CategoryViewSets(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class GoodViewSets(viewsets.ModelViewSet):
    queryset = Good.objects.all()
    serializer_class = GoodSerializer


class GoodImgsViewSets(viewsets.ModelViewSet):
    queryset = GoodImgs.objects.all()
    serializer_class = GoodImgsSerializer
