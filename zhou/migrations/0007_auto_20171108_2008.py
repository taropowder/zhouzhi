# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zhou', '0006_auto_20171108_2007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='answer_user_qq',
            field=models.TextField(default='None'),
        ),
    ]
