# Generated by Django 4.1 on 2022-10-29 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wheel', '0002_rename_teams_team'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='photo',
            field=models.ImageField(upload_to='photos'),
        ),
    ]
