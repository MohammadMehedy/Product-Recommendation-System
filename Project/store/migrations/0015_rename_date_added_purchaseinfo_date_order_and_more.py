# Generated by Django 4.1 on 2023-12-17 13:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("store", "0014_purchaseinfo_order"),
    ]

    operations = [
        migrations.RenameField(
            model_name="purchaseinfo",
            old_name="date_added",
            new_name="date_order",
        ),
        migrations.RemoveField(
            model_name="order",
            name="complete",
        ),
        migrations.RemoveField(
            model_name="order",
            name="date_order",
        ),
        migrations.RemoveField(
            model_name="order",
            name="transaction_id",
        ),
        migrations.AddField(
            model_name="purchaseinfo",
            name="complete",
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name="purchaseinfo",
            name="transaction_id",
            field=models.CharField(max_length=200, null=True),
        ),
    ]
