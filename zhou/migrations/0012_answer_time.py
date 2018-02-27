# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zhou', '0011_auto_20171108_2016'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='time',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
