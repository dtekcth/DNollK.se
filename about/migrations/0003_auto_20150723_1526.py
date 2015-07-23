# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_member_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='name',
        ),
        migrations.AddField(
            model_name='member',
            name='first_name',
            field=models.CharField(max_length=200, default='FÖRNAMN'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='member',
            name='last_name',
            field=models.CharField(max_length=200, default='EFTERNAMN'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='member',
            name='nick',
            field=models.CharField(max_length=200, default='NICK'),
            preserve_default=False,
        ),
    ]
