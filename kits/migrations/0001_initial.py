# Generated by Django 5.0.3 on 2024-04-01 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Model",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("model_id", models.IntegerField()),
                ("name", models.CharField(max_length=250)),
                ("series", models.CharField(max_length=250)),
                ("price_us", models.DecimalField(decimal_places=2, max_digits=10)),
                ("price_jp", models.DecimalField(decimal_places=0, max_digits=10)),
                ("release_date", models.DateField()),
                ("box_art", models.CharField(max_length=300)),
                ("grade", models.CharField(max_length=150)),
                ("scale", models.CharField(max_length=150)),
            ],
        ),
    ]
