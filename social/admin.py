# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *
# Register your models here.

class AdminSocialLinks(admin.ModelAdmin):
    fields = ('f_link', 't_link', 'i_link', 'y_link')
    list_display = ('title', 'f_link', 't_link', 'i_link', 'y_link')

admin.site.register(SocialLinks, AdminSocialLinks)

