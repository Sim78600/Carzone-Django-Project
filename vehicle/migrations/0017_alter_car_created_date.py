# Generated by Django 4.1 on 2022-11-01 18:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0016_alter_car_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='created_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 11, 1, 23, 9, 38, 151804)),
        ),
    ]
