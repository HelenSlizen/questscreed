# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-05-13 10:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questscreed', '0020_auto_20180512_1640'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='answer_picture',
            field=models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Изображение'),
        ),
        migrations.AddField(
            model_name='stage',
            name='stage_cover',
            field=models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Изображение'),
        ),
    ]
