# Generated by Django 4.2.5 on 2023-12-31 08:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_product_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='quatity',
            new_name='quantity',
        ),
    ]