from django.conf.urls import url

from . import views


urlpatterns =[
         url(r'^(?P<mingzi>\w{2,3})/$',views.gerenblog,name='gerenblog'),
         url(r'^service/$',views.service,name="service"),
         url(r'^(?P<post_id>\d+)/share/$',views.post_share,name='post_share'),
         url(r'^divblog/$',views.div_blog),
         url(r'^$',views.index,name='index'),
         url(r'^blog/$', views.post_list, name='post_list'),
         url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/$',views.post_detail,name='post_detail'),
         
]
