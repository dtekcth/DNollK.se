# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-07-23 16:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0006_auto_20160723_1815'),
    ]

    operations = [
        migrations.RenameField(
            model_name='committee',
            old_name='image_id',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='member',
            old_name='image_id',
            new_name='image',
        ),
    ]
