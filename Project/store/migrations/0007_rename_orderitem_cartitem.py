# Generated by Django 4.1 on 2023-12-16 16:56

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("store", "0006_rename_cart_cartit"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="OrderItem",
            new_name="CartItem",
        ),
    ]
