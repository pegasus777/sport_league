# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-10-01 09:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0008_auto_20161001_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matches',
            name='home',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='home', to='team.Team'),
        ),
    ]
