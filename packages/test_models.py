from django.test import TestCase
from .models import Package


class TestModels(TestCase):
    @classmethod
    def setUpTestData(cls):
        package = Package(
            name = 'test_name',
            description = 'test description',
            price = 100.0,
            rating = 4.0,
        )
        package.save()

    def test_package_model_saves_with_valid_data(self):
        package = Package.objects.get(id=1)

        self.assertEqual(package.name, 'test_name')
        self.assertEqual(package.description, 'test description')
        self.assertEqual(package.price, 100.0)
        self.assertEqual(package.rating, 4.0)

    def test_package(self):
        package = Package.objects.create(name='Test Package')
        self.assertEqual(str(package), 'Test Package')

    def test_item_string_method_returns_name(self):
        package = Package.objects.create(name='Package')
        self.assertEqual(str(package), 'Package')
