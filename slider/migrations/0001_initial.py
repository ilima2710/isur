# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-21 08:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=225, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a \u0441\u043b\u0430\u0439\u0434\u0430')),
                ('image', models.ImageField(upload_to='images/slider/', verbose_name='\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435 \u0441\u043b\u0430\u0439\u0434\u0430')),
                ('text', models.TextField(verbose_name='\u0422\u0435\u043a\u0441\u0442 \u0441\u043b\u0430\u0439\u0434\u0430')),
            ],
            options={
                'verbose_name': '\u0421\u043b\u0430\u0439\u0434',
                'verbose_name_plural': '\u0421\u043b\u0430\u0439\u0434\u044b',
            },
        ),
    ]