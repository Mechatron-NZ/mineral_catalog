from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'(?P<name>\d+)/$', views.detail, name='detail'),
]

