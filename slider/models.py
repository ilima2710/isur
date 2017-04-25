# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Slider(models.Model):
    class Meta:
        verbose_name = 'Слайд'
        verbose_name_plural = 'Слайды'

    title = models.CharField(max_length=225, verbose_name='Заголовок слайда')
    image = models.ImageField(upload_to='images/slider/', verbose_name='Изображение слайда')
    text = models.TextField(verbose_name='Текст слайда')

    def __unicode__(self):
        return self.title