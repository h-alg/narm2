# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hodaapp', '0004_auto_20150124_2056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='books',
            field=models.CharField(default=b'', max_length=500),
            preserve_default=True,
        ),
    ]
