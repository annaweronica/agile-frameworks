from django.test import TestCase


class TestViews(TestCase):

    def test_get_packages(self):
        response = self.client.get('/packages/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'packages/packages.html')

    def test_add_package(self):
        response = self.client.get('/packages/add/')
        self.assertEqual(response.status_code, 302)
        self.assertTemplateUsed(response, 'packages/add_package.html')
