# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zhou', '0009_remove_answer_answer_user_qq'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='answer_user_qq',
            field=models.TextField(null=True, blank=True),
        ),
    ]
