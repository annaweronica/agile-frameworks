from django.test import TestCase
from django.contrib.auth.models import User

from django.conf import settings
from django.contrib.auth import login
from django.http import HttpRequest
from django.test.client import Client
from importlib import import_module


class TestClient(Client):

    def login_user(self, user):
        user.backend = "%s.%s" % ("django.contrib.auth.backends",
                                  "ModelBackend")
        engine = import_module(settings.SESSION_ENGINE)

        # Create a fake request to store login details.
        request = HttpRequest()
        if self.session:
            request.session = self.session
        else:
            request.session = engine.SessionStore()
        login(request, user)

        # Set the cookie to represent the session.
        session_cookie = settings.SESSION_COOKIE_NAME
        self.cookies[session_cookie] = request.session.session_key
        cookie_data = {
            'max-age': None,
            'path': '/',
            'domain': settings.SESSION_COOKIE_DOMAIN,
            'secure': settings.SESSION_COOKIE_SECURE or None,
            'expires': None,
        }
        self.cookies[session_cookie].update(cookie_data)

        # Save the session values.
        request.session.save()

class TestProfileViews(TestCase):

    # test view for not loged in user
    def test_get_profile_view_without_login(self):
        response = self.client.get('/profile/')
        self.assertEqual(response.status_code, 302)
        self.assertTemplateUsed('profiles/profile.html')

    # test view for loged in user
    def test_get_profile_view_with_login(self):
        client = TestClient()
        user = User(username='testtest')
        user.save()
        client.login_user(user)

        response = self.client.get('/profile/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('profiles/profile.html')

    def test_get_order_history(self):
        response = self.client.get('order_history/<order_number>')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('checkout/checkout_success.html')
