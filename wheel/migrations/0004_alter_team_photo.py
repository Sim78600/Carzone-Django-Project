# Generated by Django 4.1 on 2022-10-29 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wheel', '0003_alter_team_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='photo',
            field=models.ImageField(upload_to='photos/%Y/%m/%d'),
        ),
    ]