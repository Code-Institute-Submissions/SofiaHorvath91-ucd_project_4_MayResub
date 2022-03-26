from django.test import TestCase
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from myappocalypse.models import Climate, Landform, Environment, Item


# Create your tests here.
class ClimateModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Climate.objects.create(name='Continental')

    def create_climate(self, name='Continental'):
        return Climate.objects.create(name=name)

    def test_name_max_length(self):
        climate = Climate.objects.get(id=1)
        max_length = climate._meta.get_field('name').max_length
        self.assertEqual(max_length, 100)

    def test_creation_climate(self):
        climate = self.create_climate()
        self.assertTrue(isinstance(climate, Climate))
        self.assertEqual(climate.name, 'Continental')


class LandformModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Landform.objects.create(name='Mountains')

    def create_landform(self, name='Mountains'):
        return Landform.objects.create(name=name)

    def test_name_max_length(self):
        landform = Landform.objects.get(id=1)
        max_length = landform._meta.get_field('name').max_length
        self.assertEqual(max_length, 100)

    def test_creation_landform(self):
        landform = self.create_landform()
        self.assertTrue(isinstance(landform, Landform))
        self.assertEqual(landform.name, 'Mountains')


class EnvironmentModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Environment.objects.create(name='Grassland')

    def create_environment(self, name='Grassland'):
        return Environment.objects.create(name=name)

    def test_name_max_length(self):
        environment = Environment.objects.get(id=1)
        max_length = environment._meta.get_field('name').max_length
        self.assertEqual(max_length, 100)

    def test_creation_environment(self):
        environment = self.create_environment()
        self.assertTrue(isinstance(environment, Environment))
        self.assertEqual(environment.name, 'Grassland')


class ItemModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        choices = Item._meta.get_field('category').choices

        climate1 = Climate.objects.create(name='Continental')
        climate2 = Climate.objects.create(name='Tropical')
        climate3 = Climate.objects.create(name='Polar')
        climates = [climate1, climate2, climate3]

        landform1 = Landform.objects.create(name='Mountains')
        landform2 = Landform.objects.create(name='Plateau')
        landforms = [landform1, landform2]

        environment1 = Environment.objects.create(name='Rocky')
        environment2 = Environment.objects.create(name='Forest')
        environment3 = Environment.objects.create(name='Grassland')
        environments = [environment1, environment2, environment3]

        Item.objects.create(name='rope', category=choices[3],
                            weight=1.00, usefulness=8.00,
                            external=True, with_child=False, with_elder=False, with_pet=False,
                            available_infrastructure=False, available_water=True, available_food=False,
                            climate=climates, landform=landforms, environment=environments)

    def test_name_category_max_length(self):
        item = Item.objects.get(id=1)
        name_max_length = item._meta.get_field('name').max_length
        category_max_length = item._meta.get_field('category').max_length
        self.assertEqual(name_max_length, 100)
        self.assertEqual(category_max_length, 30)

    def test_weight_usefulness_max_digits(self):
        item = Item.objects.get(id=1)
        weight_max_digits = item._meta.get_field('weight').max_digits
        usefulness_max_digits = item._meta.get_field('usefulness').max_digits
        self.assertEqual(weight_max_digits, 5)
        self.assertEqual(usefulness_max_digits, 5)

    def test_weight_usefulness_decimal_places(self):
        item = Item.objects.get(id=1)
        weight_decimal_places = item._meta.get_field('weight').decimal_places
        usefulness_decimal_places = item._meta.get_field('usefulness').decimal_places
        self.assertEqual(weight_decimal_places, 2)
        self.assertEqual(usefulness_decimal_places, 2)

    def test_climates(self):
        item = Item.objects.get(id=1)
        self.assertEqual(item.climate[0].name, 'Continental')
        self.assertEqual(len(item.climate), 3)

    def test_landforms(self):
        item = Item.objects.get(id=1)
        self.assertEqual(item.landform[1].name, 'Plateau')
        self.assertEqual(len(item.climate), 2)

    def test_environments(self):
        item = Item.objects.get(id=1)
        self.assertEqual(item.environment[2].name, 'Grassland')
        self.assertEqual(len(item.climate), 3)