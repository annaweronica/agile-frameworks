from django.test import TestCase


class TestViews(TestCase):

    def test_get_main_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'agile_app/main_page.html')

    def test_get_package_management(self):
        response = self.client.get('/package_management/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'agile_app/package_management.html')

    def test_get_contact(self):
        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'agile_app/contact.html')
