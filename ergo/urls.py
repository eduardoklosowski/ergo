# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as authviews

from .home import views as homeviews
from .utils import get_ergo_urls


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', authviews.login, {'template_name': 'ergohome/login.html'}, name='login'),
    url(r'^logout/$', authviews.logout, {'template_name': 'ergohome/logout.html'}, name='logout'),

    url(r'^$', homeviews.app_list, name='index'),
] + get_ergo_urls()

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
