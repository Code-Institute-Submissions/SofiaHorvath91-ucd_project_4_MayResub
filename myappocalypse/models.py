from django.db import models
from rest_framework import serializers
from django.contrib.auth import get_user_model
from ucd_project_4 import settings

# Referencing the standard Django User model
# => Aim of object/model : Capture details of connected user for login/signup function
User = get_user_model()


# Climate object/model to connect to Items (via ManyToMany relation) / Bags (via ForeignKey relation)
# => Aim of object/model : Capture details of possible climates to associate to the road where the bag will be used
class Climate(models.Model):
    name = models.CharField(blank=True, null=True, max_length=100)
    pass


# Landform object/model to connect to Items (via ManyToMany relation) / Bags (via ForeignKey relation)
# => Aim of object/model : Capture details of possible landforms to associate to the road where the bag will be used
class Landform(models.Model):
    name = models.CharField(blank=True, null=True, max_length=100)
    pass


# Environment object/model to connect to Items (via ManyToMany relation) / Bags (via ForeignKey relation)
# => Aim of object/model : Capture details of possible environments to associate to the road where the bag will be used
class Environment(models.Model):
    name = models.CharField(blank=True, null=True, max_length=100)
    pass


# Serialize climates for Item object (via ManyToMany relation)
class ClimateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Climate
        fields = '__all__'
        depth = 1


# Serialize landforms for Item object (via ManyToMany relation)
class LandformSerializer(serializers.ModelSerializer):
    class Meta:
        model = Landform
        fields = '__all__'
        depth = 1


# Serialize environments for Item object (via ManyToMany relation)
class EnvironmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Environment
        fields = '__all__'
        depth = 1


# Item object/model to connect to Bags (via ManyToMany relation)
# => Aim of object/model : Capture details of physical objects to be packed in the bag
# => Models/objects connected to Item model/object via ManyToMany relation : Climate, Landform, Environment
class Item(models.Model):
    Clothes = 'Clothes'
    Linens = 'Linens'
    Communication = 'Communication'
    Safety = 'Safety'
    Cooking = 'Cooking'
    Food_Drink = 'Food_Drink'
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
        (Food_Drink, 'Food_Drink'),
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


# Serialize items for Bag object (ManyToMany relation)
class ItemSerializer(serializers.ModelSerializer):
    climate = ClimateSerializer(many=True)
    environment = EnvironmentSerializer(many=True)
    landform = LandformSerializer(many=True)

    class Meta:
        model = Item
        fields = '__all__'
        depth = 2


# Bag object/model : Main object/model of the application
# => Aim of object/model : Capture details of bag packed for a given scenario (general details & related items)
# => Models/objects connected to Bag model/object via ManyToMany relation : Items
# => Models/objects connected to Bag model/object via ForeignKey relation : Climate, Landform, Environment, User (Owner)
class Bag(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    items = models.ManyToManyField(Item, related_name='items', blank=True)
    name = models.CharField(blank=True, null=True, max_length=50)
    weight_bag = models.DecimalField(blank=True, max_digits=5, decimal_places=2, null=True)
    weight_bag_actual = models.DecimalField(blank=True, max_digits=5, decimal_places=2, null=True)
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


# Feedback object/model
# => Aim of object/model : Capture details of feedback provided by the user about the site (rating & comment)
# => Models/objects connected to Feedback model/object via ForeignKey relation : User (Owner)
class Feedback(models.Model):
    rating_point = models.IntegerField(null=True, blank=True)
    rating_description = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)


# Recommendation object/model
# => Aim of object/model : Capture details of item recommended by a standard user for the approval of admin user
# => Models/objects connected to Recommendation model/object via ForeignKey relation : User (Owner)
class Recommendation(models.Model):
    Pending = 'Pending'
    Approved = 'Approved'
    Rejected = 'Rejected'
    STATUSES = [
        (Pending, 'Pending'),
        (Approved, 'Approved'),
        (Rejected, 'Rejected'),
    ]

    status = models.CharField(choices=STATUSES, max_length=30, default=Pending)
    category = models.CharField(blank=True, null=True, max_length=100)
    name = models.CharField(blank=True, null=True, max_length=100)
    weight = models.DecimalField(blank=True, max_digits=5, decimal_places=2, null=True)
    usefulness = models.DecimalField(blank=True, max_digits=5, decimal_places=2, null=True)
    external = models.BooleanField(blank=True, null=True, default=False)
    justification = models.TextField(blank=True, null=True, max_length=600)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)



