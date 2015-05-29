# -*- coding: utf-8 -*-
#
# Copyright 2015 Eduardo Augusto Klosowski
#
# This file is part of Ergo.
#
# Ergo is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ergo is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with Ergo.  If not, see <http://www.gnu.org/licenses/>.
#

from django.apps import apps
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as authviews

from . import views


urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', authviews.login, {'template_name': 'ergo/login.html'}, name='login'),
    url(r'^logout/', authviews.logout_then_login, name='logout'),
] + [
    url(r'^%s/' % app.ergo_url, include(app.name + '.urls'))
    for app in apps.get_app_configs() if hasattr(app, 'ergo_url')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
