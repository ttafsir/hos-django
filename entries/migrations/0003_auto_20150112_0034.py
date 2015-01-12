# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0002_auto_20150112_0026'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='serviceprovider',
            name='provider_name_cr',
        ),
        migrations.RemoveField(
            model_name='serviceprovider',
            name='provider_name_en',
        ),
        migrations.RemoveField(
            model_name='serviceprovider',
            name='provider_name_fr',
        ),
    ]
