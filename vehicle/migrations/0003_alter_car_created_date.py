# Generated by Django 4.1 on 2022-10-30 21:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0002_alter_car_created_date_alter_car_is_featured_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='created_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 10, 31, 2, 6, 59, 251839)),
        ),
    ]
