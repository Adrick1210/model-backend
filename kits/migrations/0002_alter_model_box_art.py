# Generated by Django 5.0.3 on 2024-04-02 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("kits", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="model",
            name="box_art",
            field=models.CharField(max_length=900),
        ),
    ]
