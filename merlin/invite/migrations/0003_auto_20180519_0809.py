# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-05-19 13:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('invite', '0002_auto_20171226_0938'),
    ]

    operations = [
        migrations.AddField(
            model_name='rsvp',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rsvp',
            name='food_choice',
            field=models.IntegerField(choices=[(0, 'STEAK'), (1, 'FISH'), (2, 'VEGGIE')], default=0),
        ),
        migrations.AddField(
            model_name='rsvp',
            name='song_choice',
            field=models.TextField(blank=True),
        ),
    ]
