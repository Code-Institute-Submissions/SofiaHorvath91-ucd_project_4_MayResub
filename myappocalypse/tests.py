from django.test import TestCase
from myappocalypse.models import Climate, Landform, Environment


# Create your tests here.
class ClimateModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Climate.objects.create(name='Continental')

    def test_name_max_length(self):
        climate = Climate.objects.get(id=1)
        max_length = climate._meta.get_field('name').max_length
        self.assertEqual(max_length, 100)
