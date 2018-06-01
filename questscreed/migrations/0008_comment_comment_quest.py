# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-05-01 12:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questscreed', '0007_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='comment_quest',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='questscreed.Quest'),
        ),
    ]