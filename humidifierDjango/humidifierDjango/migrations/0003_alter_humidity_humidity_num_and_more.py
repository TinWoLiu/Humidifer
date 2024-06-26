# Generated by Django 4.1 on 2024-04-07 19:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("humidifierDjango", "0002_humidity_time_created_humidity_time_updated"),
    ]

    operations = [
        migrations.AlterField(
            model_name="humidity",
            name="humidity_num",
            field=models.DecimalField(decimal_places=4, max_digits=7),
        ),
        migrations.AlterField(
            model_name="temperature",
            name="temperature_num",
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
