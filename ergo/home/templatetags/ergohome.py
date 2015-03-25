# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django import template
from django.conf import settings
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.core.urlresolvers import reverse

from ...utils import get_ergo_app_configs


register = template.Library()


@register.simple_tag
def ergohome_applist():
    html = []
    for app in get_ergo_app_configs():
        if hasattr(app, 'ergo_url_index') and (not hasattr(app, 'ergo_hide_app') or not app.ergo_hide_app):
            if hasattr(app, 'ergo_verbose_name'):
                verbose_name = app.ergo_verbose_name
            else:
                verbose_name = app.verbose_name
            html.append((verbose_name, '<li><a href="%s">%s</a></li>' % (reverse(app.ergo_url_index), verbose_name)))
    html.sort(key=lambda x: x[0])
    return ''.join([i[1] for i in html])


@register.simple_tag
def ergohome_icon():
    if hasattr(settings, 'ERGOHOME_ICON'):
        return '<link rel="shortcut icon" href="%s">' % static(settings.ERGOHOME_ICON)
    return ''


@register.simple_tag
def ergohome_title():
    if hasattr(settings, 'ERGOHOME_TITLE'):
        return settings.ERGOHOME_TITLE
    return 'Ergo'
