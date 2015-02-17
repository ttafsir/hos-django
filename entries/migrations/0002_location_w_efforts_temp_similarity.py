# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='location_w_efforts_temp',
            name='similarity',
            field=models.CharField(max_length=100, null=True),
            preserve_default=True,
        ),
    ]
