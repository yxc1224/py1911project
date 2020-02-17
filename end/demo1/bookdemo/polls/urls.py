from django.conf.urls import url
from . import views

app_name = "polls"

urlpatterns = [
    # 基于函数的路由
    # url(r'^$', views.polls, name='polls'),
    # url(r'^addpolls/(\d+)/$', views.addpolls, name='addpolls'),
    # url(r'^ballot/(\d+)/$', views.ballot, name='ballot')

    # 基于类的路由
    url(r'^$',views.IndexView.as_view(),name='polls'),
    url(r'^addpolls/(\d+)/$',views.Detailview.as_view(),name='addpolls'),
    url(r'^ballot/(\d+)/$',views.ResultView.as_view(),name='ballot')
]
