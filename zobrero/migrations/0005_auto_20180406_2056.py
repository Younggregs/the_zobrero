# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-04-06 20:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zobrero', '0004_remove_employee_what_do_you_do'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
