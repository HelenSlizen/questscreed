# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-05-13 12:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questscreed', '0021_auto_20180513_1355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quest',
            name='complexity',
            field=models.CharField(choices=[('Легко', 'Легко'), ('Средне', 'Средне'), ('Сложно', 'Сложно')], default='Легко', max_length=200),
        ),
        migrations.AlterField(
            model_name='quest',
            name='quest_type',
            field=models.CharField(choices=[('Классический квест', 'Классический квест'), ('Квест-экскурсия', 'Квест-экскурсия'), ('Авто-квест', 'Авто-квест')], default='Квест-экскурсия', max_length=200),
        ),
    ]