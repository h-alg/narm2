# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id_book', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('edition', models.IntegerField(default=1)),
                ('field', models.CharField(default=b'AR', max_length=100, choices=[(b'UN', b'University'), (b'AR', b'Art'), (b'SC', b'Science'), (b'KD', b'Kids')])),
                ('price', models.IntegerField(default=0)),
                ('rate', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
