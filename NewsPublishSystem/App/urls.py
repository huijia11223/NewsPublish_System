from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^index/$',views.index),
    url(r'^login/$',views.login),
    url(r'^register/$',views.register),
    url(r'^quit/$',views.quit),
    url(r'^mine/(\d+)/$',views.mine), 
    url(r'^updateMaterial/(\d+)/$',views.updateMaterial),
    url(r'^index2/(\d+)/$',views.index2)
]