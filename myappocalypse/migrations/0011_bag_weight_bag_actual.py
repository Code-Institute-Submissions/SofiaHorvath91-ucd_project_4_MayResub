# Generated by Django 4.0.2 on 2022-03-20 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myappocalypse', '0010_alter_item_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='bag',
            name='weight_bag_actual',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
    ]
