# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-05-15 13:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questscreed', '0030_statistic_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statistic',
            name='time',
            field=models.TextField(blank=True, null=True),
        ),
    ]
