# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zhou', '0012_answer_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='original_anwser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('original_answer_user_qq', models.BigIntegerField(null=True, blank=True)),
                ('original_time', models.CharField(max_length=30, null=True)),
                ('original_answer_text', models.TextField()),
                ('original_quesion_answer', models.ForeignKey(related_name='original_answer', to='zhou.Question')),
            ],
        ),
        migrations.RemoveField(
            model_name='answer',
            name='answer_user_qq',
        ),
    ]
