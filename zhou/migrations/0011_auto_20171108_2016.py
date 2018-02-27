# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zhou', '0010_answer_answer_user_qq'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='answer_user_qq',
            field=models.BigIntegerField(null=True, blank=True),
        ),
    ]
