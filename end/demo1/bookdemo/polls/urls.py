from django.conf.urls import url
from . import views

app_name="polls"

urlpatterns=[
    url(r'^$',views.polls,name='polls'),
    url(r'^addpolls/(\d+)/$',views.addpolls,name='addpolls'),
    url(r'ballot/(\d+)/$',views.ballot,name='ballot')
]