from django.test import TestCase
from .forms import OrderForm


class TestOrderForm(TestCase):

    def test_order_full_name_is_required_fields(self):
        form = OrderForm({'full_name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('full_name', form.errors.keys())
        self.assertEqual(form.errors['full_name'][0], 'This field is required.')
