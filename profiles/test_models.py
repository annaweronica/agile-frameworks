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
        profile = UserProfile.objects.get(id=userprofile.id)

        # self.assertEqual(userprofile.user, 'user')
        self.assertEqual(profile.default_town_or_city, 'town_or_city')
        self.assertEqual(profile.default_street_address1, 'street_address1')
        self.assertEqual(profile.default_street_address2, 'street_address2')
        self.assertEqual(profile.default_country, 'Sweden')

    def test_item_string_method_returns_name(self):
        user = UserProfile.objects.create(name='Test User')
        self.assertEqual(str(user), 'Test User')

# the test are not run. Error: not null constraint failed: 
# profiels_userprofile.user_id