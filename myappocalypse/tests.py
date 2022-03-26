import decimal

from django.test import TestCase
from myappocalypse.models import Climate, Landform, Environment, Item, Bag, Feedback, Recommendation


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

        item = Item.objects.create(name='rope', category=choices[3],
                            weight=1.00, usefulness=8.00,
                            external=True, with_child=False, with_elder=False, with_pet=False,
                            available_infrastructure=False, available_water=True, available_food=False)
        item.climate.set(climates)
        item.landform.set(landforms)
        item.environment.set(environments)

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
        climate_list = []
        for clm in item.climate.all():
            climate_list.append(clm.name)
        self.assertEqual(climate_list[0], 'Continental')
        self.assertEqual(len(climate_list), 3)

    def test_landforms(self):
        item = Item.objects.get(id=1)
        landform_list = []
        for lf in item.landform.all():
            landform_list.append(lf.name)
        self.assertEqual(landform_list[1], 'Plateau')
        self.assertEqual(len(landform_list), 2)

    def test_environments(self):
        item = Item.objects.get(id=1)
        environment_list = []
        for env in item.environment.all():
            environment_list.append(env.name)
        self.assertEqual(environment_list[2], 'Grassland')
        self.assertEqual(len(environment_list), 3)

    def test_choices(self):
        item = Item.objects.get(id=1)
        choices = Item._meta.get_field('category').choices
        self.assertEqual(choices[5][0], 'Food_Drink')
        self.assertEqual(len(choices), 12)
        self.assertEqual(str(choices[3]), item.category)


class BagModelTest(TestCase):
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

        item1 = Item.objects.create(name='rope', category=choices[3], weight=1.00, usefulness=8.00,
                                    external=True, with_child=False, with_elder=False, with_pet=False,
                                    available_infrastructure=False, available_water=True, available_food=False)
        item1.climate.set(climates)
        item1.landform.set(landforms)
        item1.environment.set(environments)

        item2 = Item.objects.create(name='radio', category=choices[2], weight=0.50, usefulness=9.00,
                                    external=False, with_child=False, with_elder=False, with_pet=False,
                                    available_infrastructure=True, available_water=False, available_food=False)
        item2.climate.set(climates)
        item2.landform.set(landforms)
        item2.environment.set(environments)

        items = [item1, item2]
        items_weight = 0
        for i in items:
            items_weight += i.weight
        weight_user = 56
        weight_bag = round((weight_user * 0.2) + 1, 2)

        bag = Bag.objects.create(name='my_bag',
                                 weight_user=weight_user, weight_bag=weight_bag, weight_bag_actual=items_weight,
                                 climate=climate1, landform=landform1, environment=environment1,
                                 with_child=False, with_elder=False, with_pet=False,
                                 available_infrastructure=True, available_water=False, available_food=False)
        bag.items.set(items)

    def test_name_category_max_length(self):
        bag = Bag.objects.get(id=1)
        name_max_length = bag._meta.get_field('name').max_length
        self.assertEqual(name_max_length, 50)

    def test_weight_fields_max_digits(self):
        bag = Bag.objects.get(id=1)
        weight_bag_max_digits = bag._meta.get_field('weight_bag').max_digits
        weight_bag_actual_max_digits = bag._meta.get_field('weight_bag_actual').max_digits
        weight_user_max_digits = bag._meta.get_field('weight_user').max_digits
        self.assertEqual(weight_bag_max_digits, 5)
        self.assertEqual(weight_bag_actual_max_digits, 5)
        self.assertEqual(weight_user_max_digits, 5)

    def test_weight_fields_decimal_places(self):
        bag = Bag.objects.get(id=1)
        weight_bag_decimal_places = bag._meta.get_field('weight_bag').decimal_places
        weight_bag_actual_decimal_places = bag._meta.get_field('weight_bag_actual').decimal_places
        weight_user_decimal_places = bag._meta.get_field('weight_user').decimal_places
        self.assertEqual(weight_bag_decimal_places, 2)
        self.assertEqual(weight_bag_actual_decimal_places, 2)
        self.assertEqual(weight_user_decimal_places, 2)

    def test_user_weight_bag_weight(self):
        bag = Bag.objects.get(id=1)
        self.assertEqual(bag.weight_bag, round(decimal.Decimal(float(bag.weight_user) * 0.2 + 1), 2))

    def test_actual_bag_weight(self):
        bag = Bag.objects.get(id=1)
        items_weight = 0
        for i in bag.items.all():
            items_weight += i.weight
        self.assertEqual(bag.weight_bag_actual, items_weight)

    def test_climate_landform_environment(self):
        bag = Bag.objects.get(id=1)

        bag_climate_all_items = 0
        bag_landform_all_items = 0
        bag_environment_all_items = 0
        for i in bag.items.all():
            if bag.climate in i.climate.all():
                bag_climate_all_items += 1
            if bag.landform in i.landform.all():
                bag_landform_all_items += 1
            if bag.environment in i.environment.all():
                bag_environment_all_items += 1

        self.assertEqual(bag.climate.name, 'Continental')
        self.assertEqual(bag.landform.name, 'Mountains')
        self.assertEqual(bag.environment.name, 'Rocky')
        self.assertEqual(bag.items.count(), 2)
        self.assertEqual(bag_climate_all_items, bag.items.count())
        self.assertEqual(bag_landform_all_items, bag.items.count())
        self.assertEqual(bag_environment_all_items, bag.items.count())