# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-12-25 16:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='fan_votes',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
