# Generated by Django 4.1 on 2023-12-16 17:35

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("store", "0008_rename_order_cart"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="cart",
            name="complete",
        ),
        migrations.RemoveField(
            model_name="cart",
            name="transaction_id",
        ),
        migrations.DeleteModel(
            name="cartIt",
        ),
    ]
