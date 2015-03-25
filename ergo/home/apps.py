# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class ErgoHomeConfig(AppConfig):
    name = 'ergo.home'
    verbose_name = _('Ergo Home')
    ergo_url = 'home'
    ergo_verbose_name = _('Home')
