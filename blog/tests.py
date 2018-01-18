# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase, Client

class HomePageTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_home_page_kinda_works(self):
        """Ensure the homepage returns a status code indicating success."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
