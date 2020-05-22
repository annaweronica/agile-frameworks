from django.test import TestCase
from django.contrib.auth.models import User

from django.conf import settings
from django.contrib.auth import login
from django.http import HttpRequest
from django.test.client import Client
from importlib import import_module


class TestProfileViews(TestCase):

    # test view for not loged in user
    def test_get_profile_view_with_user_logged_in(self):
        user = User.objects.create(username='testuser')
        user.set_password('SecretUser123')
        user.save()
        logged_in = self.client.login(username='testuser', password='SecretUser123')
        response = self.client.get('/profile/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('profiles/profile.html')

    def test_unauthenticated_user_cannot_get_profile_view(self):
        response = self.client.get('/profile/')
        self.assertEqual(response.status_code, 302)
