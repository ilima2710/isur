# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import *

class NewsAdmin(admin.ModelAdmin):
    fields = ['title', 'image', 'preview', 'text']
    # exclude = ['preview', 'text']
    list_display = ['title', 'preview']




admin.site.register(News, NewsAdmin)


