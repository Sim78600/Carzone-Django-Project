# Generated by Django 4.1 on 2022-11-06 22:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0028_alter_car_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='created_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 11, 7, 3, 55, 49, 441358)),
        ),
    ]
