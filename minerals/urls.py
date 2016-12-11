from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='list'),
    url(r'^random/$', views.random_mineral, name='random'),
    url(r'^(?P<name>[\w,\d()\s-]+)/$', views.mineral_detail, name='detail'),

]
