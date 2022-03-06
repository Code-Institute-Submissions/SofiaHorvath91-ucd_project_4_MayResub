from django.db import models
from django.conf import settings
from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.validators import UniqueValidator

User = get_user_model()


class Climate(models.Model):
    name = models.CharField(blank=True, null=True, max_length=100)
    pass


class Landform(models.Model):
    name = models.CharField(blank=True, null=True, max_length=100)
    pass


class Environment(models.Model):
    name = models.CharField(blank=True, null=True, max_length=100)
    pass


class ClimateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Climate
        fields = '__all__'
        depth = 1


class LandformSerializer(serializers.ModelSerializer):

    class Meta:
        model = Landform
        fields = '__all__'
        depth = 1


class EnvironmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Environment
        fields = '__all__'
        depth = 1


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

    category = models.CharField(choices=CATEGORIES, max_length=30)
    name = models.CharField(blank=True, null=True, max_length=100)
    weight = models.DecimalField(blank=True, max_digits=5, decimal_places=2, null=True)
    usefulness = models.DecimalField(blank=True, max_digits=5, decimal_places=2, null=True)
    external = models.BooleanField(blank=True, null=True, default=False)
    climate = models.ManyToManyField(Climate, related_name='climates', blank=True)
    landform = models.ManyToManyField(Landform, related_name='landforms', blank=True)
    environment = models.ManyToManyField(Environment, related_name='environments', blank=True)
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
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    items = models.ManyToManyField(Item, related_name='items', blank=True)
    name = models.CharField(blank=True, null=True, max_length=50)
    weight_bag = models.DecimalField(blank=True, max_digits=5, decimal_places=2, null=True)
    weight_user = models.DecimalField(blank=True, max_digits=5, decimal_places=2, null=True)
    climate = models.ForeignKey(Climate, on_delete=models.CASCADE)
    landform = models.ForeignKey(Landform, on_delete=models.CASCADE)
    environment = models.ForeignKey(Environment, on_delete=models.CASCADE)
    with_child = models.BooleanField(blank=True, null=True)
    with_elder = models.BooleanField(blank=True, null=True)
    with_pet = models.BooleanField(blank=True, null=True)
    available_infrastructure = models.BooleanField(blank=True, null=True)
    available_water = models.BooleanField(blank=True, null=True)
    available_food = models.BooleanField(blank=True, null=True)