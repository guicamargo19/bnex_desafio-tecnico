# Generated by Django 5.0.4 on 2024-05-03 12:46

import products.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_product_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='value',
            field=models.DecimalField(decimal_places=2, max_digits=10, validators=[products.models.non_negative_validator]),
        ),
    ]
