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

from django.conf.urls import include, url

from . import views


url_list = [
    url(r'^$', views.IndexView.as_view(), name='index'),

    url(r'^notify/$', views.NotifyListView.as_view(), name='notify_list'),
]

urlpatterns = [
    url('', include(url_list, namespace='ergohome')),
]
