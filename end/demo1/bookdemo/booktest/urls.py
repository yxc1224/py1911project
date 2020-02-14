from django.conf.urls import url
from . import views

app_name="booktest"

#  每个路由文件中都要有urlpatterns这个路由数组
urlpatterns=[
    url(r'^$',views.index,name='index'),
    url(r'^about/$',views.about,name='about'),
    url(r'^detail/(\d+)/$',views.detail,name='detail'),
    url(r'^deletebook/(\d+)/$',views.deletebook,name='deletebook'),
    url(r'^deletehero/(\d+)/$',views.deletehero,name='deletehero'),
    url(r'^addhero/(\d+)/$',views.addhero,name='addhero'),
    url(r'^edithero/(\d+)/$',views.edithero,name='edithero')
]