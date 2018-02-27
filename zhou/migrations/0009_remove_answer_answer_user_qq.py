# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zhou', '0008_auto_20171108_2010'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='answer_user_qq',
        ),
    ]
