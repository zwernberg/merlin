# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-05-22 11:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invite', '0006_auto_20180520_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guest',
            name='food_choice',
            field=models.IntegerField(choices=[(0, 'STEAK'), (1, 'SALMON'), (2, 'PENNE'), (3, 'KIDS'), (999, 'NONE')], default=999),
        ),
        migrations.AlterField(
            model_name='rsvp',
            name='food_choice',
            field=models.IntegerField(choices=[(0, 'STEAK'), (1, 'SALMON'), (2, 'PENNE'), (3, 'KIDS'), (999, 'NONE')], default=999),
        ),
    ]
