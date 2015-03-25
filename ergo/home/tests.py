# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.apps import apps
from django.conf import settings
from django.core.urlresolvers import reverse
from django.test import Client, TestCase

from .templatetags import ergohome


class ErgoHomeTagsTest(TestCase):
    def test_applist(self):
        html = ergohome.ergohome_applist()
        if html:
            self.assertTrue(html.startswith('<li>'))

    def test_icon(self):
        html = ergohome.ergohome_icon()
        if html:
            self.assertTrue(html.startswith('<link '))

    def test_title(self):
        self.assertTrue(ergohome.ergohome_title())


class ErgoHomeViewsTest(TestCase):
    def setUp(self):
        User = apps.get_model(settings.AUTH_USER_MODEL)
        user = User(username='admin')
        user.set_password('password')
        user.save()

        self.client = Client()
        self.client.login(username='admin', password='password')

    def test_applist(self):
        response = self.client.get(reverse('ergohome:index'))
        self.assertTrue(response.status_code, 200)
