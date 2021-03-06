# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-30 15:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0002_auto_20160930_0442'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coach',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coach_name', models.CharField(max_length=250)),
                ('DOB', models.DateField()),
                ('country', models.CharField(max_length=200)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('coach_image', models.FileField(upload_to='')),
                ('coach_team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='team.Team')),
            ],
        ),
    ]
