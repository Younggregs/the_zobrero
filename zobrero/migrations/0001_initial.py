# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-04-05 17:11
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(default='anonymous', max_length=30)),
                ('lastname', models.CharField(default='anonymous', max_length=30)),
                ('username', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=50)),
                ('profile_pic', models.FileField(default='anon.png', upload_to=b'')),
                ('rating', models.IntegerField()),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField()),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zobrero.Account')),
            ],
        ),
        migrations.CreateModel(
            name='ImageReservoir',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to=b'')),
            ],
        ),
        migrations.CreateModel(
            name='Talent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('talent', models.CharField(max_length=100)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zobrero.Category')),
            ],
        ),
        migrations.CreateModel(
            name='VideoReservoir',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(upload_to=b'')),
            ],
        ),
        migrations.CreateModel(
            name='WhatCanYouDo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zobrero.Employee')),
                ('talent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zobrero.Talent')),
            ],
        ),
        migrations.CreateModel(
            name='WhatHaveYouDone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zobrero.Employee')),
            ],
        ),
        migrations.AddField(
            model_name='videoreservoir',
            name='whyd',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zobrero.WhatHaveYouDone'),
        ),
        migrations.AddField(
            model_name='imagereservoir',
            name='whyd',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zobrero.WhatHaveYouDone'),
        ),
        migrations.AddField(
            model_name='employee',
            name='what_do_you_do',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zobrero.Talent'),
        ),
    ]
