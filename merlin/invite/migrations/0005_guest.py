# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-05-20 03:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('invite', '0004_auto_20180519_0820'),
    ]

    operations = [
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('food_choice', models.IntegerField(choices=[(0, 'STEAK'), (1, 'FISH'), (2, 'VEGGIE'), (3, 'KIDS'), (999, 'NONE')], default=999)),
                ('rsvp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='guests', to='invite.RSVP')),
            ],
        ),
    ]
