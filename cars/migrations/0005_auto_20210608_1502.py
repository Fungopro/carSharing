# Generated by Django 3.2 on 2021-06-08 09:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0004_auto_20210608_1500'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Users',
            new_name='Cars',
        ),
        migrations.RenameField(
            model_name='drive',
            old_name='user',
            new_name='car',
        ),
        migrations.AlterField(
            model_name='drive',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 8, 15, 2, 56, 870398), verbose_name='Время поездки'),
        ),
        migrations.AlterField(
            model_name='drive',
            name='drive_to',
            field=models.CharField(default='', max_length=100),
        ),
    ]
