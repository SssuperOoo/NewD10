# Generated by Django 5.0.3 on 2024-04-01 07:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('simpleapp', '0003_remove_product_material_product_product_material'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='product_material',
            new_name='material',
        ),
    ]
