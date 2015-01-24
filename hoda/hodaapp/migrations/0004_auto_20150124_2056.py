# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hodaapp', '0003_auto_20150124_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='hesab',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
