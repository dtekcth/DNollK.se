# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='number',
            field=models.CharField(max_length=50, default='NULL'),
            preserve_default=False,
        ),
    ]
