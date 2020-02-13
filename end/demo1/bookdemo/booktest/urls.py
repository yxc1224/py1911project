from django.conf.urls import url
from . import views
#  每个路由文件中都要有urlpatterns这个路由数组
urlpatterns=[
    url(r'^index/$',views.index),
    # url(r'^about/$',views.about),
    url(r'^detail/(\d+)/',views.detail)
]