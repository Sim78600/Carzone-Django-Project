# Generated by Django 4.1 on 2022-10-30 21:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0006_alter_car_created_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='description',
        ),
        migrations.AlterField(
            model_name='car',
            name='created_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 10, 31, 2, 24, 41, 488006)),
        ),
    ]
