from django.test import TestCase
from .models import Packages


class TestModels(TestCase):

    def test_package(self):
        packages = Packages.objects.create(name='Test Package')
        self.assertFalse(packages.done)
