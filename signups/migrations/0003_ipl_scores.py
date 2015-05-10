# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('signups', '0002_auto_20150508_1836'),
    ]

    operations = [
        migrations.CreateModel(
            name='ipl_scores',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Detail', models.TextField(max_length=200)),
                ('Score1', models.TextField(max_length=40)),
                ('Score2', models.TextField(max_length=40)),
            ],
        ),
    ]
