from django.test import TestCase
from .models import Order
from django.test import Client


class TestViews(TestCase):

    def test_checkout(self):
        c = Client()
        c.login(username='testuser', password='SecretTest123')

        response = self.client.get('/checkout/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout/checkout.html')
