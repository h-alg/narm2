# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import multiselectfield.db.fields
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('hodaapp', '0002_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='books',
            field=models.CharField(default=datetime.datetime(2015, 1, 24, 12, 3, 0, 555000, tzinfo=utc), max_length=500),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='users',
            name='favorite',
            field=multiselectfield.db.fields.MultiSelectField(max_length=11, choices=[(b'AR', b'art'), (b'SC', b'science'), (b'UN', b'university'), (b'KD', b'kids')]),
            preserve_default=True,
        ),
    ]
