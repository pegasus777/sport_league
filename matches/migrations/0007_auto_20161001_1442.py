# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-10-01 09:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0006_auto_20161001_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matches',
            name='away',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='away', to='team.Team'),
        ),
        migrations.AlterField(
            model_name='matches',
            name='home',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='home', to='team.Team'),
        ),
        migrations.AlterField(
            model_name='matches',
            name='result',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='result', to='team.Team'),
        ),
    ]
