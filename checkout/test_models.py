from django.test import TestCase
from .models import Order

# Create your tests here.


class TestModels(TestCase):
    @classmethod
    def setUpTestData(cls):
        order = Order(
            order_number = '123654',
            name = 'test_name',
            full_name = 'John Smith',
            email = 'test@test.com',
            town_or_city = 'Test City',
            street_address1 = 'Test Street 1',
            street_address2 = 'Test Street 2',
            total = 123
        )
        order.save()

    def test_order_model_saves_with_valid_data(self):
        order = Order.objects.get(id=1)

        self.assertEqual(order.order_number, '123654')
        self.assertEqual(order.name, 'test_name')
        self.assertEqual(order.full_name, 'John Smith')
        self.assertEqual(order.email, 'test@test.com')
        self.assertEqual(order.town_or_city, 'Test City')
        self.assertEqual(order.street_address1, 'Test Street 1')
        self.assertEqual(order.street_address2, 'Test Street 2')
        self.assertEqual(order.total, 123)

    def test_order_model_name_displays_correctly(self):
        order = Order.objects.get(id=1)
        self.assertEqual(str(order), '123654')
