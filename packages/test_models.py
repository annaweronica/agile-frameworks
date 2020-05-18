from django.test import TestCase
from .models import Package


class TestModels(TestCase):

    def test_package(self):
        package = Package.objects.create(name='Test Package')
        self.assertEqual(str(package), 'Test Package')
