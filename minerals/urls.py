from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='list'),
    url(r'^(?P<name>\d+)/$', views.mineral_detail, name='detail'),
]

