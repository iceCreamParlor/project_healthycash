# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import  HealthClub, HealthDiary, HealthClubDetailReply

# Register your models here.

admin.site.register(HealthClub)
admin.site.register(HealthDiary)
admin.site.register(HealthClubDetailReply)