# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import geoposition.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20150605_0908'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='position',
            field=geoposition.fields.GeopositionField(max_length=42, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='coffee',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'None'), (1, b'Instant'), (2, b'Average'), (3, b'Good'), (4, b'Phenomenal!')]),
        ),
    ]
