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

import os

from .core import *  # NOQA


BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


SECRET_KEY = 'ergo'
DEBUG = True
ALLOWED_HOSTS = []

TIME_ZONE = 'UTC'

try:
    import debug_toolbar  # NOQA
    INSTALLED_APPS += (
        'debug_toolbar',
    )
except ImportError:
    pass

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

BOWER_COMPONENTS_ROOT = os.path.join(BASE_DIR, 'components')

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
