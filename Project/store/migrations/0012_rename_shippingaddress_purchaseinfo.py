# Generated by Django 4.1 on 2023-12-17 04:07

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("store", "0011_rename_cartitem_orderitem_alter_orderitem_order_and_more"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="ShippingAddress",
            new_name="PurchaseInfo",
        ),
    ]
