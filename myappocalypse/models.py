from django.db import models
from django.conf import settings
from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.validators import UniqueValidator

User = get_user_model()


class Item(models.Model):
    Clothes = 'Clothes'
    Linens = 'Linens'
    Communication = 'Communication'
    Safety = 'Safety'
    Cooking = 'Cooking'
    Food = 'Food'
    Drink = 'Drink'
    Hygiene = 'Hygiene'
    Health = 'Health'
    Lightning = 'Lightning'
    Orientation = 'Orientation'
    Tools = 'Tools'
    Weapons = 'Weapons'
    CATEGORIES = [
        (Clothes, 'Clothes'),
        (Linens, 'Linens'),
        (Communication, 'Communication'),
        (Safety, 'Safety'),
        (Cooking, 'Cooking'),
        (Food, 'Food'),
        (Drink, 'Drink'),
        (Hygiene, 'Hygiene'),
        (Health, 'Health'),
        (Lightning, 'Lightning'),
        (Orientation, 'Orientation'),
        (Tools, 'Tools'),
        (Weapons, 'Weapons'),
    ]

    Dry = 'Dry'
    Tropical = 'Tropical'
    Continental = 'Continental'
    Temperate = 'Temperate'
    Polar = 'Polar'
    CLIMATE_TYPES = [
        (Dry, 'Dry'),
        (Tropical, 'Tropical'),
        (Continental, 'Continental'),
        (Temperate,'Temperate'),
        (Polar, 'Polar'),
    ]

    Mountains = 'Mountains'
    Hills = 'Hills'
    Plateau = 'Plateau'
    Plain = 'Plain'
    Ocean = 'Ocean'
    LANDFORM_TYPES = [
        (Mountains, 'Mountains'),
        (Hills, 'Hills'),
        (Plateau, 'Plateau'),
        (Plain, 'Plain'),
        (Ocean, 'Ocean'),
    ]

    Forest = 'Forest'
    Rocky = 'Rocky'
    Grassland = 'Grassland'
    Desert = 'Desert'
    Tundra = 'Tundra'
    Marine = 'Marine'
    ENVIRONMENT_TYPES = [
        (Forest, 'Forest'),
        (Rocky, 'Rocky'),
        (Grassland, 'Grassland'),
        (Desert, 'Desert'),
        (Tundra, 'Tundra'),
        (Marine, 'Marine'),
    ]

    category = models.CharField(choices=CATEGORIES, max_length=30)
    weight = models.DecimalField(blank=True, max_digits=5, decimal_places=2, null=True)
    usefulness = models.DecimalField(blank=True, max_digits=5, decimal_places=2, null=True)
    climate = models.CharField(choices=CLIMATE_TYPES, max_length=30)
    landform = models.CharField(choices=LANDFORM_TYPES, max_length=30)
    environment = models.CharField(choices=ENVIRONMENT_TYPES, max_length=30)
    with_child = models.BooleanField(blank=True, null=True)
    with_elder = models.BooleanField(blank=True, null=True)
    with_pet = models.BooleanField(blank=True, null=True)
    available_infrastructure = models.BooleanField(blank=True, null=True)
    available_water = models.BooleanField(blank=True, null=True)
    available_food = models.BooleanField(blank=True, null=True)
    pass


class ItemSerializer(serializers.ModelSerializer):
    users = UniqueValidator(queryset=User.objects.all())

    class Meta:
        model = Item
        fields = '__all__'
        depth = 1


class Bag(models.Model):
    Dry = 'Dry'
    Tropical = 'Tropical'
    Continental = 'Continental'
    Temperate = 'Temperate'
    Polar = 'Polar'
    CLIMATE_TYPES = [
        (Dry, 'Dry'),
        (Tropical, 'Tropical'),
        (Continental, 'Continental'),
        (Temperate,'Temperate'),
        (Polar, 'Polar'),
    ]

    Mountains = 'Mountains'
    Hills = 'Hills'
    Plateau = 'Plateau'
    Plain = 'Plain'
    Ocean = 'Ocean'
    LANDFORM_TYPES = [
        (Mountains, 'Mountains'),
        (Hills, 'Hills'),
        (Plateau, 'Plateau'),
        (Plain, 'Plain'),
        (Ocean, 'Ocean'),
    ]

    Forest = 'Forest'
    Rocky = 'Rocky'
    Grassland = 'Grassland'
    Desert = 'Desert'
    Tundra = 'Tundra'
    Marine = 'Marine'
    ENVIRONMENT_TYPES = [
        (Forest, 'Forest'),
        (Rocky, 'Rocky'),
        (Grassland, 'Grassland'),
        (Desert, 'Desert'),
        (Tundra, 'Tundra'),
        (Marine, 'Marine'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    items = models.ManyToManyField(Item, related_name='items', blank=True)
    name = models.TextField(blank=True, null=True)
    weight_bag = models.DecimalField(blank=True, max_digits=5, decimal_places=2, null=True)
    weight_user = models.DecimalField(blank=True, max_digits=5, decimal_places=2, null=True)
    climate = models.CharField(choices=CLIMATE_TYPES, max_length=30)
    landform = models.CharField(choices=LANDFORM_TYPES, max_length=30)
    environment = models.CharField(choices=ENVIRONMENT_TYPES, max_length=30)
    with_child = models.BooleanField(blank=True, null=True)
    with_elder = models.BooleanField(blank=True, null=True)
    with_pet = models.BooleanField(blank=True, null=True)
    available_infrastructure = models.BooleanField(blank=True, null=True)
    available_water = models.BooleanField(blank=True, null=True)
    available_food = models.BooleanField(blank=True, null=True)