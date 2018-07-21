# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-07-14 23:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('zobrero', '0007_auto_20180711_2149'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='AppointmentDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appm_date', models.DateField()),
                ('appm_time', models.TimeField()),
                ('appointment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zobrero.Appointment')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zobrero.Talent')),
            ],
        ),
        migrations.CreateModel(
            name='AppointmentStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.CharField(max_length=200)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('appointment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zobrero.Appointment')),
            ],
        ),
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_2', models.IntegerField()),
                ('delete_for_1', models.BooleanField(default=False)),
                ('delete_for_2', models.BooleanField(default=False)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('favorite', models.IntegerField()),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='ForgotPassword',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('reset_code', models.CharField(default='123579', max_length=30)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Messenger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('seen', models.BooleanField(default=False)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('ehaggler', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zobrero.Chat')),
            ],
            options={
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='RateReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client', models.IntegerField()),
                ('rating', models.IntegerField()),
                ('review', models.CharField(max_length=150)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='RecentActivity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=100)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.AlterField(
            model_name='account',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='account',
            name='phone',
            field=models.CharField(max_length=11),
        ),
        migrations.AlterField(
            model_name='calls',
            name='caller',
            field=models.CharField(max_length=11),
        ),
        migrations.AlterField(
            model_name='calls',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='calls',
            name='receiver',
            field=models.CharField(max_length=11),
        ),
        migrations.AlterField(
            model_name='employee',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='employee',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='whathaveyoudone',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='recentactivity',
            name='account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zobrero.Account'),
        ),
        migrations.AddField(
            model_name='recentactivity',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zobrero.Employee'),
        ),
        migrations.AddField(
            model_name='ratereview',
            name='account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zobrero.Account'),
        ),
        migrations.AddField(
            model_name='messenger',
            name='messenger',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zobrero.Account'),
        ),
        migrations.AddField(
            model_name='favorite',
            name='account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zobrero.Account'),
        ),
        migrations.AddField(
            model_name='chat',
            name='account_1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zobrero.Account'),
        ),
        migrations.AddField(
            model_name='appointmentstatus',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zobrero.Status'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zobrero.Employee'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='employer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zobrero.Account'),
        ),
    ]
