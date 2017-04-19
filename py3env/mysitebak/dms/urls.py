from django.conf.urls import url

from . import views

urlpatterns = [
        url(r'^$',views.loginview,name='login'),
        url(r'^login/$',views.loginview,name='login'),
        url(r'^regist/$',views.registview,name='regist'),
        url(r'^index/$',views.indexview,name='index'),
        url(r'^logout/$',views.logoutview,name='logout'),
        ]
