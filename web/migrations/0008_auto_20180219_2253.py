# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-02-19 22:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_housingevaluation_niming'),
    ]

    operations = [
        migrations.AlterField(
            model_name='housingevaluation',
            name='niming',
            field=models.IntegerField(choices=[(0, '\u533f\u540d'), (1, '\u6b63\u5e38')], default=0, verbose_name='\u533f\u540d'),
        ),
    ]
