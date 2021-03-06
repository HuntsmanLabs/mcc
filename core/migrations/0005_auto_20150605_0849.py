# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='alcohol',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'No'), (1, b'Yes')]),
        ),
        migrations.AddField(
            model_name='location',
            name='coffee',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'None'), (1, b'crap'), (2, b'Average'), (3, b'Good'), (4, b'Phenomenal!')]),
        ),
        migrations.AddField(
            model_name='location',
            name='food',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'No'), (1, b'Yes')]),
        ),
        migrations.AddField(
            model_name='location',
            name='freelancer',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'No'), (1, b'Yes')]),
        ),
        migrations.AddField(
            model_name='location',
            name='outdoor',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'No'), (1, b'Yes')]),
        ),
        migrations.AddField(
            model_name='location',
            name='outlets',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'None'), (1, b'Minimal'), (2, b'Some'), (3, b'Heaps')]),
        ),
        migrations.AddField(
            model_name='location',
            name='seating',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'None'), (1, b'Minimal'), (2, b'Some'), (3, b'Heaps')]),
        ),
        migrations.AddField(
            model_name='location',
            name='wifi',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'None'), (1, b'Free (Hooray!)'), (2, b'Paid')]),
        ),
    ]
