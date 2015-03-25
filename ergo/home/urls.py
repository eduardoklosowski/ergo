# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf.urls import include, url

from . import views


url_list = [
    url(r'^$', views.app_list, name='index'),
    url(r'^apps/$', views.app_list, name='app_list')
]

urlpatterns = [
    url('', include(url_list, namespace='ergohome')),
]
