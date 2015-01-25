# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('hodaapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('username', models.CharField(max_length=100, serialize=False, primary_key=True)),
                ('password', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('birthday_date', models.DateField(auto_now_add=True)),
                ('adress', models.CharField(max_length=500)),
                ('hesab', models.IntegerField()),
                ('favorite', multiselectfield.db.fields.MultiSelectField(max_length=3, choices=[(1, b'art'), (2, b'science')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
