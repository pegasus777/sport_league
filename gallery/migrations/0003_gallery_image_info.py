# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-06 17:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_remove_gallery_image_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='image_info',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]
