# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-12-24 23:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0029_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='housingresources',
            name='click_count',
            field=models.IntegerField(default=0, verbose_name='\u70b9\u51fb\u91cf'),
        ),
        migrations.AddField(
            model_name='housingresources',
            name='hot',
            field=models.IntegerField(choices=[(0, '\u5426'), (1, '\u662f')], default=0, verbose_name='\u6700\u70ed'),
        ),
    ]
