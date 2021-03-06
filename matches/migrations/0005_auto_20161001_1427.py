# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-10-01 08:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0004_auto_20161001_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matches',
            name='away',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='aways', to='team.Team'),
        ),
        migrations.AlterField(
            model_name='matches',
            name='home',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='homes', to='team.Team'),
        ),
        migrations.AlterField(
            model_name='matches',
            name='result',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='results', to='team.Team'),
        ),
    ]
