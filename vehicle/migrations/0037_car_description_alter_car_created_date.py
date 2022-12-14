# Generated by Django 4.1 on 2022-11-11 02:26

import ckeditor.fields
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0036_alter_car_created_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='created_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 11, 11, 7, 26, 31, 916986)),
        ),
    ]
