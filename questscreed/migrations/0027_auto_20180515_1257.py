# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-05-15 09:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questscreed', '0026_statistic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statistic',
            name='end_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='statistic',
            name='time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]