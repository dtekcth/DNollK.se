# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.files.storage


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='upload',
            name='name',
            field=models.CharField(max_length=100, default='NULL'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='upload',
            name='photo',
            field=models.ImageField(storage=django.core.files.storage.FileSystemStorage(location='/home/taira/Projects/Python/DNollK/static2/uploads/'), upload_to=''),
        ),
    ]
