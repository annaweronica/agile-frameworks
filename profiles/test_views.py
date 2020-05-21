from django.test import TestCase
from django.contrib.auth.models import User

from django.conf import settings
from django.contrib.auth import login
from django.http import HttpRequest
from django.test.client import Client
from importlib import import_module


class TestProfileViews(TestCase):

    # test view for not loged in user
    def test_get_profile_view_without_login(self):
        response = self.client.get('/profile/')
        self.assertEqual(response.status_code, 302)
        self.assertTemplateUsed('profiles/profile.html')

    # test view for loged in user
    def test_get_profile_view_with_login(self):
        c = Client()
        c.login(username='testuser', password='SecretTest123')

        response = self.client.get('/profile/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('profiles/profile.html')

    def test_get_order_history(self):
        response = self.client.get('order_history/<order_number>')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('checkout/checkout_success.html')

    def test_user_logged_in(self):
        c = Client()
        response = c.post('./login/', {'username': 'testuser', 'password': 'SecretUser123'})
        self.assertEqual(response.status_code, 200)
        print(response.status_code)
