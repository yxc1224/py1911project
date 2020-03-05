"""drfend URL Configuration

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
from django.conf.urls import url
from .settings import MEDIA_ROOT
from shop.views import *
from django.views.static import serve

#  引入API文档路由
from rest_framework.documentation import include_docs_urls

# 引入rest_framework_simple路由
from rest_framework_simplejwt.views import token_obtain_pair, token_refresh

# 引入DRF自带的路由类
from rest_framework import routers

router = routers.DefaultRouter()

# router.register('categorys', CategoryViewSets2,basename='categorys')
router.register('categorys', CategoryViewSets)
router.register('goods', GoodViewSets)
router.register('goodimgs', GoodImgsViewSets)
router.register('users', UserViewSet)
router.register('orders', OrderViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    url('media/(?P<path>.*)', serve, {'document_root': MEDIA_ROOT}),

    # 基于函数的路由
    # url(r'^categorylist/$', categoryList, name='categorylist'),
    # url(r'^categorydetail/(\d+)/$', categoryDetail, name='categorydetail'),

    # 基于类的路由
    # url(r'^categorylist/$', CategoryListView.as_view(), name='categorylist'),
    # url(r'^categorydetail/(\d+)/$', CategoryDetailView.as_view(), name='categorydetail'),

    # url(r'^categorylist/$', CategoryListView2.as_view(), name='categorylist'),
    # url(r'^categorydetail/(?P<pk>\d+)/$', CategoryDetailView2.as_view(), name='categorydetail'),

    # url(r'^categorys/$', CategoryViewSets2.as_view({'get': 'list','post':'create'})),
    # url(r'^categorys/(?P<pk>\d+)/$', CategoryViewSets2.as_view({'get': 'retrieve','put':'update','patch':'update','delete':'destroy'})),

    # 先通过用户名密码得到Token VUE得到refresh以及access保存  通过access请求服务器  通过refresh获取新的access
    url(r'^login/$', token_obtain_pair, name='login'),
    url('^refresh/$', token_refresh, name='refresh'),

    path('api/v1/', include(router.urls)),
    path('api/v1/docs/', include_docs_urls(title="RestFulAPI", description='RestFulAPIv1')),
    path('', include('rest_framework.urls')),
]
