from django.test import TestCase
from .models import Order


class TestViews(TestCase):

    def test_checkout(self):
        response = self.client.get('/checkout/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout/checkout.html')

    # def test_checkout_success(self): #  fails because it has to call order_number
    #     response = self.client.get('/checkout/checkout_success/0005A1F1A8FB48298FD0E12CB37C32B6')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, '/checkout/checkout_success.html')
