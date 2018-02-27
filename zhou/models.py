# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Question(models.Model):
    qustion_user = models.ForeignKey(User)
    content = models.TextField(null=False)
    time = models.CharField(max_length=30)
    def __unicode__(self):  # 在Python3中用 __str__ 代替 __unicode__
        return self.content
class Answer(models.Model):
    quesion_answer = models.ForeignKey(Question,related_name='answer')
    answer_rank = models.IntegerField()
    time = models.CharField(max_length=30,null=True)
    answer_text = models.TextField(default='还没有接收到答案,请稍等')
    def __unicode__(self):  # 在Python3中用 __str__ 代替 __unicode__
        return self.quesion_answer.content
class User_info(models.Model):
    user_connect = models.ForeignKey(User,related_name='info')
    user_qq = models.CharField(max_length=30,null=True)
    user_integral = models.IntegerField(default="0")
    def __unicode__(self):  # 在Python3中用 __str__ 代替 __unicode__
        return self.user_connect.username
class Original_Anwser(models.Model):
    original_quesion_answer = models.ForeignKey(Question,related_name='original_answer')
    original_answer_user_id = models.BigIntegerField(blank=True, null=True)
    original_time = models.CharField(max_length=30, null=True)
    original_answer_text = models.TextField()
    def __unicode__(self):  # 在Python3中用 __str__ 代替 __unicode__
        return self.original_quesion_answer.content

