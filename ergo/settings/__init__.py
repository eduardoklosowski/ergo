# -*- coding: utf-8 -*-

from __future__ import unicode_literals

try:
    from .dev import *  # NOQA
except ImportError:
    from .defaults import *  # NOQA
