# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-05-11 17:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questscreed', '0018_stage_stage_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stage',
            name='stage_number',
            field=models.IntegerField(default=1),
        ),
    ]
