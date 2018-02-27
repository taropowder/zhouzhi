# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from zhou.models import Answer,Question,User_info,Original_Anwser

# Register your models here.
admin.site.register(Answer)
admin.site.register(Question)
admin.site.register(User_info)
admin.site.register(Original_Anwser)