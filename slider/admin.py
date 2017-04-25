from django.contrib import admin
from .models import *

# Register your models here.
class SliderAdmin(admin.ModelAdmin):
    fields = ['title', 'image', 'text']
    list_display = ['title', 'image']

admin.site.register(Slider, SliderAdmin)
