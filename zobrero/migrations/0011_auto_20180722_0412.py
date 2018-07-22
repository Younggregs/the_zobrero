# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-07-22 04:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zobrero', '0010_auto_20180721_0142'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointmentdetail',
            name='appm_date',
        ),
        migrations.RemoveField(
            model_name='appointmentdetail',
            name='appm_time',
        ),
        migrations.AddField(
            model_name='appointmentdetail',
            name='appointment_date',
            field=models.CharField(default='1/8', max_length=20),
        ),
        migrations.AddField(
            model_name='appointmentdetail',
            name='appointment_time',
            field=models.CharField(default='12:00:00am', max_length=20),
        ),
        migrations.AddField(
            model_name='appointmentdetail',
            name='description',
            field=models.TextField(default='description'),
        ),
    ]
