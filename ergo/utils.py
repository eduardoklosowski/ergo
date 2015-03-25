# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.apps import apps
from django.conf.urls import include, url


def get_ergo_app_configs():
    return [app for app in apps.get_app_configs() if hasattr(app, 'ergo_url')]


def get_ergo_notifications():
    return [app for app in apps.get_app_configs() if hasattr(app, 'ergo_notifications')]


def get_ergo_urls():
    return [url(r'^%s/' % app.ergo_url, include('%s.urls' % app.name))
            for app in get_ergo_app_configs()]
