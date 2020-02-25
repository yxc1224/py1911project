from  django.conf.urls import url,include
from . import views

app_name='blogapp'

urlpatterns=[

    url(r'^$',views.index,name='index'),
    url(r'^detail/(\d+)/$',views.detail,name='detail'),
    url(r'^contact/$',views.contact,name='contact'),
    url(r'^favicon.ico/$',views.favicon),
    url(r'^search/', include('haystack.urls')),
]