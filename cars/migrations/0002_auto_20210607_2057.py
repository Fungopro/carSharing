# Generated by Django 3.2 on 2021-06-07 14:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drive',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 7, 20, 57, 27, 560278), verbose_name='Время поездки'),
        ),
        migrations.AlterField(
            model_name='driver',
            name='birth_date',
            field=models.DateField(verbose_name='Birth date'),
        ),
        migrations.AlterField(
            model_name='users',
            name='birth_date',
            field=models.DateField(verbose_name='Birth date'),
        ),
    ]
