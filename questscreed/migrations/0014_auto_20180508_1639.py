# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-05-08 13:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questscreed', '0013_auto_20180508_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quest',
            name='quest_city',
            field=models.CharField(choices=[('SP', 'Санкт-Петербург')], default='SP', max_length=2),
        ),
    ]