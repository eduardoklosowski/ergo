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

from __future__ import unicode_literals

from django import template
from django.apps import apps
from django.shortcuts import resolve_url


register = template.Library()


@register.simple_tag
def ergohome_nav_applications():
    applications = [(getattr(app, 'verbose_name', app.name),
                     resolve_url(app.ergo_index),
                     getattr(app, 'ergo_menu_links', ()))
                    for app in apps.get_app_configs() if hasattr(app, 'ergo_index')]
    applications.sort(key=lambda x: x[0].lower())
    html = []
    for app in applications:
        if app[2]:
            links = ('<li><a href="%s">%s</a></li>' % (link[1], link[0]) for link in app[2])
            html.append('<li class="has-dropdown"><a href="%s">%s</a><ul class="dropdown">%s</ul></li>' %
                        (app[1], app[0], ''.join(links)))
        else:
            html.append('<li><a href="%s">%s</a></li>' % (app[1], app[0]))
    return ''.join(html)
