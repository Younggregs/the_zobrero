# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-04-08 00:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zobrero', '0005_auto_20180406_2056'),
    ]

    operations = [
        migrations.AddField(
            model_name='talent',
            name='adjective',
            field=models.CharField(default='i can work', max_length=100),
        ),
    ]