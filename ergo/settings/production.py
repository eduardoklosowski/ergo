# -*- coding: utf-8 -*-

import os

from ergo.settings.core import *  # NOQA


BASE_DIR = os.path.dirname(os.path.abspath(__file__))


SECRET_KEY = ''
DEBUG = False
ALLOWED_HOSTS = ['*']

TIME_ZONE = 'UTC'

# INSTALLED_APPS += (
#     'ergonotes',
# )

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'CONN_MAX_AGE': 600,
    }
}

BOWER_COMPONENTS_ROOT = os.path.join(BASE_DIR, 'components')

COMPRESS_OFFLINE = True

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# Optimizations

SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'

del TEMPLATES[0]['APP_DIRS']
TEMPLATES[0]['OPTIONS']['loaders'] = [
    ('django.template.loaders.cached.Loader', [
        'django.template.loaders.app_directories.Loader',
    ]),
]
