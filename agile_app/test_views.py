from django.test import TestCase


class TestViews(TestCase):

    def test_get_main_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'agile_app/main_page.html')
