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

from django.apps import apps
from django.core.urlresolvers import reverse_lazy
from django.views import generic

from ..views import LoginRequiredMixin


class IndexView(LoginRequiredMixin, generic.RedirectView):
    permanent = False
    url = reverse_lazy('ergohome:notify_list')


class NotifyListView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'ergohome/notify_list.html'

    def get_context_data(self, **kwargs):
        ergo_apps = [app for app in apps.get_app_configs() if hasattr(app, 'ergo_notify')]
        ergo_apps.sort(key=lambda x: x.verbose_name)
        notify_list = []
        for app in ergo_apps:
            for notify in app.ergo_notify(self.request):
                notify_list.append(notify)

        context = super(NotifyListView, self).get_context_data(**kwargs)
        context['notify_list'] = notify_list
        return context
