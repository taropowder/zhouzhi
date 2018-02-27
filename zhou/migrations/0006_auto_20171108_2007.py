# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('zhou', '0005_auto_20171022_1034'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_info',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_qq', models.CharField(max_length=30, null=True)),
                ('user_integral', models.IntegerField(default='0')),
                ('user_connect', models.ForeignKey(related_name='info', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='answer',
            name='answer_user_qq',
            field=models.TextField(default=None),
        ),
    ]
