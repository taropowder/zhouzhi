# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zhou', '0013_auto_20171209_1609'),
    ]

    operations = [
        migrations.RenameField(
            model_name='original_anwser',
            old_name='original_answer_user_qq',
            new_name='original_answer_user_id',
        ),
    ]
