from django.test import TestCase
from .models import UserProfile


class TestModels(TestCase):
    @classmethod
    def setUpTestData(cls):
        userprofile = UserProfile(
            # user = 'user',
            default_town_or_city = 'town_or_city',
            default_street_address1 = 'street_address1',
            default_street_address2 = 'street_address2',
            default_country = 'Sweden'
        )
        userprofile.save()

    def test_userprofile_model_saves_with_valid_data(self):
        userprofile = UserProfile.objects.get(id=1)

        # self.assertEqual(userprofile.user, 'user')
        self.assertEqual(userprofile.default_town_or_city, 'town_or_city')
        self.assertEqual(userprofile.default_street_address1, 'street_address1')
        self.assertEqual(userprofile.default_street_address2, 'street_address2')
        self.assertEqual(userprofile.default_country, 'Sweden')

    def test_userprofile(self):
        user = UserProfile.objects.create(name='Test User')
        self.assertEqual(str(user), 'Test User')

    def test_item_string_method_returns_name(self):
        package = Package.objects.create(name='Package')
        self.assertEqual(str(package), 'Package')

# run 0 test, fails
