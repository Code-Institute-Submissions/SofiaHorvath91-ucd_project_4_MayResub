from django.test import TestCase
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
        landform = Landform.objects.create(name='Mountains')
        climate = Climate.objects.create(name='Continental')
        environment = Environment.objects.create(name='Rocky')
        Item.objects.create(name='rope', category=choices[3],
                            weight=1.00, usefulness=8.00,
                            external=True, with_child=False, with_elder=False, with_pet=False,
                            available_infrastructure=False, available_water=True, available_food=False,
                            climate=climate, landform=landform, environment=environment)

    def test_name_category_max_length(self):
        item = Item.objects.get(id=1)
        name_max_length = item._meta.get_field('name').max_length
        category_max_length = item._meta.get_field('category').max_length
        self.assertEqual(name_max_length, 100)
        self.assertEqual(category_max_length, 30)