# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from ..utils import get_ergo_notifications


@login_required
def app_list(request):
    app_configs = get_ergo_notifications()
    app_configs.sort(key=lambda x: x.verbose_name)

    apps_notifications = []
    for app in app_configs:
        for notification in app.ergo_notifications(request):
            apps_notifications.append(notification)

    return render(request, 'ergohome/app_list.html', {
        'apps_notifications': apps_notifications,
    })
