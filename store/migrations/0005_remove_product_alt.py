# Generated by Django 4.1.2 on 2022-10-31 15:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_remove_product_slug_product_alt_alter_product_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='alt',
        ),
    ]
