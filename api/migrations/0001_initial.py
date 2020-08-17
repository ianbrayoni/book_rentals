# Generated by Django 2.2 on 2020-08-17 13:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Invoices",
            fields=[
                ("id", models.UUIDField(primary_key=True, serialize=False)),
                ("date_generated", models.DateTimeField()),
                ("total_charges", models.DecimalField(decimal_places=2, max_digits=12)),
            ],
        ),
        migrations.CreateModel(
            name="Rentals",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("book_id", models.IntegerField()),
                ("duration", models.IntegerField()),
                ("quantity", models.IntegerField()),
                ("rental_date", models.DateTimeField()),
                ("charge", models.DecimalField(decimal_places=2, max_digits=12)),
                (
                    "invoice",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="api.Invoices"
                    ),
                ),
            ],
        ),
    ]