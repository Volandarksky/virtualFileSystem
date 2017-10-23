from django.conf.urls import url, include
from django.contrib import admin
from vfs import views

urlpatterns = [
    url(r'^$', views.vfs, name='vfs'),
    url(r'^(?P<folder_path>\w+)/$', views.dirs, name='dirs'),
]
