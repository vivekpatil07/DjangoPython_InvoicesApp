# Generated by Django 4.0.1 on 2024-01-03 17:11

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("invoices", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="invoicedetail",
            name="price",
        ),
    ]
