# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0003_auto_20150112_0034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='effortinstance',
            name='location',
            field=models.OneToOneField(null=True, blank=True, to='entries.Location'),
            preserve_default=True,
        ),
    ]
