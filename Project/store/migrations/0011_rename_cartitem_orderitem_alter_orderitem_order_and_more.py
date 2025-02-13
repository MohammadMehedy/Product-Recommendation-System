# Generated by Django 4.1 on 2023-12-16 17:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("store", "0010_cart_complete_cart_transaction_id_order"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="CartItem",
            new_name="OrderItem",
        ),
        migrations.AlterField(
            model_name="orderitem",
            name="order",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="store.order",
            ),
        ),
        migrations.AlterField(
            model_name="shippingaddress",
            name="order",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="store.order",
            ),
        ),
        migrations.DeleteModel(
            name="Cart",
        ),
    ]
