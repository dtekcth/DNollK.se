# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('arr', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='arr',
            name='location',
            field=models.CharField(default='NULL', max_length=100),
            preserve_default=False,
        ),
    ]
