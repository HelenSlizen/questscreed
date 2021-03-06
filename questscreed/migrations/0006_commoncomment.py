# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-05-01 12:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('questscreed', '0005_quest_quest_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommonComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('common_comment_author', models.CharField(max_length=200)),
                ('common_comment_text', models.TextField()),
                ('common_comment_created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('common_comment_approved_comment', models.BooleanField(default=False)),
            ],
        ),
    ]
