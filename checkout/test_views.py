from django.test import TestCase


class TestViews(TestCase):

    def test_checkout(self):
        response = self.client.get('/checkout/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout/checkout.html')
