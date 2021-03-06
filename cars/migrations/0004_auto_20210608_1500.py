# Generated by Django 3.2 on 2021-06-08 09:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_auto_20210608_1445'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='birth_date',
            new_name='car_date',
        ),
        migrations.RenameField(
            model_name='users',
            old_name='user_id',
            new_name='car_id',
        ),
        migrations.RenameField(
            model_name='users',
            old_name='user_name',
            new_name='car_name',
        ),
        migrations.RemoveField(
            model_name='driver',
            name='car',
        ),
        migrations.AddField(
            model_name='users',
            name='car_number',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='users',
            name='car_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='drive',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 8, 15, 0, 27, 784839), verbose_name='Время поездки'),
        ),
    ]
