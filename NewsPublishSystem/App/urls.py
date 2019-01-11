from django.conf.urls import url
from . import views

urlpatterns=[
    #普通用户
    url(r'^index/$',views.index),
    url(r'^login/$',views.login),
    url(r'^register/$',views.register),
    url(r'^quit/$',views.quit),
    url(r'^mine/(\d+)/$',views.mine), 
    url(r'^initMaterial/(\d+)/$',views.initMaterial),
    url(r'^index2/(\d+)/$',views.index2),
    url(r'^ModifyData/(\d+)/$',views.ModifyData),
    url(r'^military/$',views.military),
    url(r'^science/$',views.science),

    #新闻发布者
    url(r'^newPublisherLogin/$',views.newPublisherLogin),
    url(r'^publisherExit/$',views.publisherExit),
]