# Generated by Django 4.0.4 on 2022-05-15 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_product_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('appetizers', 'appetizers'), ('enterees', 'entrees'), ('treats', 'treats'), ('drinks', 'drinks')], max_length=60),
        ),
    ]
