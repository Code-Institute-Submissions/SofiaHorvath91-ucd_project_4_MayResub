# Generated by Django 4.0.2 on 2022-03-13 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myappocalypse', '0008_alter_item_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('Clothes', 'Clothes'), ('Linens', 'Linens'), ('Communication', 'Communication'), ('Safety', 'Safety'), ('Cooking', 'Cooking'), ('Food', 'Food_Drink'), ('Hygiene', 'Hygiene'), ('Health', 'Health'), ('Lightning', 'Lightning'), ('Orientation', 'Orientation'), ('Tools', 'Tools'), ('Weapons', 'Weapons')], max_length=30),
        ),
    ]
