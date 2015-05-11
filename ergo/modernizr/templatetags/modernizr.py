# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django import template
from django.conf import settings
from django.contrib.staticfiles.templatetags.staticfiles import static


include_js = '<script src="%s"></script>'
register = template.Library()


@register.simple_tag
def modernizr():
    return include_js % static('modernizr/modernizr.js')
