# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-02-10 15:50
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_del', models.BooleanField(default=False, verbose_name='\u662f\u5426\u5220\u9664')),
                ('is_valid', models.BooleanField(default=True, verbose_name='\u662f\u5426\u53ef\u7528')),
                ('updated', models.DateTimeField(auto_now=True, null=True, verbose_name='\u66f4\u65b0\u65f6\u95f4')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('name', models.CharField(default='', max_length=128, verbose_name='\u7ba1\u7406\u5458\u540d\u79f0')),
                ('ip', models.CharField(default='', max_length=128, verbose_name='\u7ba1\u7406\u5458IP')),
                ('admin_id', models.IntegerField(blank=True, default=0, null=True, verbose_name='\u7ba1\u7406\u5458ID')),
            ],
            options={
                'verbose_name': '\u7ba1\u7406\u5458\u767b\u5f55\u8bb0\u5f55',
                'verbose_name_plural': '\u7ba1\u7406\u5458\u767b\u5f55\u8bb0\u5f55',
            },
        ),
        migrations.CreateModel(
            name='Advertising',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_del', models.BooleanField(default=False, verbose_name='\u662f\u5426\u5220\u9664')),
                ('is_valid', models.BooleanField(default=True, verbose_name='\u662f\u5426\u53ef\u7528')),
                ('updated', models.DateTimeField(auto_now=True, null=True, verbose_name='\u66f4\u65b0\u65f6\u95f4')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('name', models.CharField(max_length=128, verbose_name='\u540d\u79f0')),
                ('order_no', models.IntegerField(default=0, verbose_name='\u6392\u5e8f\u53f7')),
                ('img', models.CharField(blank=True, default='', max_length=1024, verbose_name='\u56fe\u7247')),
                ('target_url', models.CharField(max_length=300, verbose_name='\u94fe\u63a5\u5730\u5740')),
                ('intro', models.TextField(blank=True, default='', verbose_name='\u7b80\u4ecb')),
            ],
            options={
                'verbose_name': '\u8f6e\u64ad\u56fe',
                'verbose_name_plural': '\u8f6e\u64ad\u56fe',
            },
        ),
        migrations.CreateModel(
            name='Bedroom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_del', models.BooleanField(default=False, verbose_name='\u662f\u5426\u5220\u9664')),
                ('is_valid', models.BooleanField(default=True, verbose_name='\u662f\u5426\u53ef\u7528')),
                ('updated', models.DateTimeField(auto_now=True, null=True, verbose_name='\u66f4\u65b0\u65f6\u95f4')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('area', models.FloatField(blank=True, default=0, verbose_name='\u9762\u79ef')),
                ('complete', models.CharField(blank=True, default='', max_length=1024, verbose_name='\u914d\u5957')),
                ('cover', models.CharField(blank=True, default='', max_length=1024, verbose_name='\u56fe\u7247')),
                ('status', models.IntegerField(choices=[(0, '\u672a\u51fa\u79df'), (1, '\u5df2\u51fa\u79df')], default=0, verbose_name='\u72b6\u6001')),
            ],
            options={
                'verbose_name': '\u623f\u5c4b\u5367\u5ba4',
                'verbose_name_plural': '\u623f\u5c4b\u5367\u5ba4',
            },
        ),
        migrations.CreateModel(
            name='Column',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_del', models.BooleanField(default=False, verbose_name='\u662f\u5426\u5220\u9664')),
                ('is_valid', models.BooleanField(default=True, verbose_name='\u662f\u5426\u53ef\u7528')),
                ('updated', models.DateTimeField(auto_now=True, null=True, verbose_name='\u66f4\u65b0\u65f6\u95f4')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('name', models.CharField(max_length=128, verbose_name='\u540d\u79f0')),
                ('order_no', models.IntegerField(default=0, verbose_name='\u6392\u5e8f\u53f7')),
                ('slug', models.CharField(default='', max_length=128, verbose_name='slug')),
                ('cover', models.CharField(blank=True, default='', max_length=1024, verbose_name='\u56fe\u7247')),
            ],
            options={
                'verbose_name': '\u680f\u76ee',
                'verbose_name_plural': '\u680f\u76ee',
            },
        ),
        migrations.CreateModel(
            name='FeedBack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_del', models.BooleanField(default=False, verbose_name='\u662f\u5426\u5220\u9664')),
                ('is_valid', models.BooleanField(default=True, verbose_name='\u662f\u5426\u53ef\u7528')),
                ('updated', models.DateTimeField(auto_now=True, null=True, verbose_name='\u66f4\u65b0\u65f6\u95f4')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('content', models.TextField(default='', verbose_name='\u53cd\u9988\u5185\u5bb9')),
                ('user', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='\u7528\u6237')),
            ],
            options={
                'verbose_name': '\u610f\u89c1\u53cd\u9988',
                'verbose_name_plural': '\u610f\u89c1\u53cd\u9988',
            },
        ),
        migrations.CreateModel(
            name='HouseConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_del', models.BooleanField(default=False, verbose_name='\u662f\u5426\u5220\u9664')),
                ('is_valid', models.BooleanField(default=True, verbose_name='\u662f\u5426\u53ef\u7528')),
                ('updated', models.DateTimeField(auto_now=True, null=True, verbose_name='\u66f4\u65b0\u65f6\u95f4')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('order_no', models.IntegerField(default=0, verbose_name='\u6392\u5e8f\u53f7')),
                ('name', models.CharField(blank=True, default='', max_length=1024, verbose_name='\u540d\u79f0')),
            ],
            options={
                'verbose_name': '\u623f\u95f4\u914d\u7f6e',
                'verbose_name_plural': '\u623f\u95f4\u914d\u7f6e',
            },
        ),
        migrations.CreateModel(
            name='HousingPicture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_del', models.BooleanField(default=False, verbose_name='\u662f\u5426\u5220\u9664')),
                ('is_valid', models.BooleanField(default=True, verbose_name='\u662f\u5426\u53ef\u7528')),
                ('updated', models.DateTimeField(auto_now=True, null=True, verbose_name='\u66f4\u65b0\u65f6\u95f4')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('picture', models.CharField(blank=True, default='', max_length=1024, verbose_name='\u56fe\u7247')),
            ],
            options={
                'verbose_name': '\u623f\u5c4b\u56fe\u7247',
                'verbose_name_plural': '\u623f\u5c4b\u56fe\u7247',
            },
        ),
        migrations.CreateModel(
            name='HousingResources',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_del', models.BooleanField(default=False, verbose_name='\u662f\u5426\u5220\u9664')),
                ('is_valid', models.BooleanField(default=True, verbose_name='\u662f\u5426\u53ef\u7528')),
                ('updated', models.DateTimeField(auto_now=True, null=True, verbose_name='\u66f4\u65b0\u65f6\u95f4')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('cover', models.CharField(blank=True, default='', max_length=1024, verbose_name='\u56fe\u7247')),
                ('house_pcover', models.CharField(blank=True, default='', max_length=1024, verbose_name='\u623f\u4ea7\u8bc1')),
                ('hall', models.CharField(blank=True, default='', max_length=1024, verbose_name='\u5927\u5385\u56fe\u7247')),
                ('peripheral', models.TextField(blank=True, default='', null=True, verbose_name='\u914d\u5957\u8bbe\u65bd')),
                ('lease', models.IntegerField(choices=[(0, '\u6574\u79df'), (1, '\u5408\u79df')], default=0, verbose_name='\u79df\u8d41\u65b9\u5f0f')),
                ('month_rent', models.FloatField(default=0, verbose_name='\u6708\u79df\u91d1')),
                ('bet', models.FloatField(default=0, verbose_name='\u62bc')),
                ('pay', models.FloatField(default=0, verbose_name='\u4ed8')),
                ('direction', models.IntegerField(choices=[(0, '\u4e1c'), (1, '\u5357'), (2, '\u897f'), (3, '\u5317')], default=0, verbose_name='\u697c\u5c42\u671d\u5411')),
                ('sitting_room', models.IntegerField(choices=[(0, '\u6709'), (1, '\u65e0')], default=0, verbose_name='\u6709\u65e0\u5ba2\u5385')),
                ('sitting_room_area', models.FloatField(blank=True, default=0, verbose_name='\u5ba2\u5385\u9762\u79ef')),
                ('sitting_room_complete', models.CharField(blank=True, default='', max_length=1024, verbose_name='\u5ba2\u5385\u914d\u5957')),
                ('layer', models.IntegerField(default=0, verbose_name='\u5c42\u6570')),
                ('province', models.CharField(blank=True, default='', max_length=32, null=True, verbose_name='\u7701')),
                ('city', models.CharField(blank=True, default='', max_length=32, null=True, verbose_name='\u5e02')),
                ('area', models.CharField(blank=True, default='', max_length=32, null=True, verbose_name='\u533a')),
                ('total_layer', models.IntegerField(default=0, verbose_name='\u603b\u5c42\u6570')),
                ('category', models.CharField(blank=True, default='', max_length=1024, verbose_name='\u623f\u5c4b\u7c7b\u578b')),
                ('community', models.CharField(blank=True, default='', max_length=1024, verbose_name='\u5c0f\u533a\u540d\u79f0')),
                ('address', models.CharField(blank=True, default='', max_length=1024, verbose_name='\u8be6\u7ec6\u5730\u5740')),
                ('bus', models.CharField(blank=True, default='', max_length=1024, verbose_name='\u516c\u4ea4')),
                ('subway', models.CharField(blank=True, default='', max_length=1024, verbose_name='\u5730\u94c1')),
                ('buy', models.CharField(blank=True, default='', max_length=1024, verbose_name='\u8d2d\u7269')),
                ('content', models.TextField(blank=True, default='', null=True, verbose_name='\u623f\u5c4b\u63cf\u8ff0')),
                ('status', models.IntegerField(choices=[(0, ''), (1, '\u4e0b\u7ebf'), (2, '\u4e0a\u7ebf')], default=0, verbose_name='\u72b6\u6001')),
                ('audit_status', models.IntegerField(choices=[(0, '\u5f85\u5ba1\u6838'), (1, '\u5ba1\u6838\u4e0d\u901a\u8fc7'), (2, '\u5ba1\u6838\u901a\u8fc7')], default=0, verbose_name='\u5ba1\u6838\u72b6\u6001')),
                ('click_count', models.IntegerField(default=0, verbose_name='\u70b9\u51fb\u91cf')),
                ('hot', models.IntegerField(choices=[(0, '\u5426'), (1, '\u662f')], default=0, verbose_name='\u6700\u70ed')),
                ('lng', models.FloatField(default=0, verbose_name='\u7ecf\u5ea6')),
                ('lat', models.FloatField(default=0, verbose_name='\u7eac\u5ea6')),
            ],
            options={
                'verbose_name': '\u623f\u6e90\u53d1\u5e03',
                'verbose_name_plural': '\u623f\u6e90\u53d1\u5e03',
            },
        ),
        migrations.CreateModel(
            name='HousingResourcesComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_del', models.BooleanField(default=False, verbose_name='\u662f\u5426\u5220\u9664')),
                ('is_valid', models.BooleanField(default=True, verbose_name='\u662f\u5426\u53ef\u7528')),
                ('updated', models.DateTimeField(auto_now=True, null=True, verbose_name='\u66f4\u65b0\u65f6\u95f4')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('content', models.TextField(blank=True, default='', null=True, verbose_name='\u623f\u5c4b\u63cf\u8ff0')),
                ('housing_resources', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='web.HousingResources', verbose_name='\u623f\u6e90')),
            ],
            options={
                'verbose_name': '\u623f\u6e90\u5ba1\u6838\u8bc4\u8bba',
                'verbose_name_plural': '\u623f\u6e90\u5ba1\u6838\u8bc4\u8bba',
            },
        ),
        migrations.CreateModel(
            name='HousingResourcesOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_del', models.BooleanField(default=False, verbose_name='\u662f\u5426\u5220\u9664')),
                ('is_valid', models.BooleanField(default=True, verbose_name='\u662f\u5426\u53ef\u7528')),
                ('updated', models.DateTimeField(auto_now=True, null=True, verbose_name='\u66f4\u65b0\u65f6\u95f4')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('order_num', models.CharField(blank=True, default='', max_length=128, verbose_name='\u552f\u4e00\u8ba2\u5355\u53f7')),
                ('total_fee', models.FloatField(blank=True, default=0, verbose_name='\u603b\u8ba1\u91d1\u989d')),
                ('real_fee', models.FloatField(blank=True, default=0, verbose_name='\u5b9e\u9645\u4ed8\u6b3e')),
                ('pay_way', models.IntegerField(choices=[(0, '\u652f\u4ed8\u5b9dPC\u7f51\u7ad9\u652f\u4ed8'), (1, '\u5fae\u4fe1App\u652f\u4ed8'), (2, '\u652f\u4ed8\u5b9d\u79fb\u52a8\u652f\u4ed8'), (3, '\u652f\u4ed8\u5b9d\u624b\u673a\u7f51\u7ad9\u652f\u4ed8')], default=0, verbose_name='\u652f\u4ed8\u65b9\u5f0f')),
                ('pay_time', models.DateTimeField(auto_now=True, verbose_name='\u652f\u4ed8\u65f6\u95f4')),
                ('charge_id', models.CharField(blank=True, default='', max_length=300, verbose_name='ping++\u652f\u4ed8id')),
                ('status', models.IntegerField(choices=[(0, '\u5f85\u4e0b\u5355'), (1, '\u7b49\u5f85\u4ed8\u6b3e'), (2, '\u4ed8\u6b3e\u6210\u529f'), (3, '\u8ba2\u5355\u53d6\u6d88'), (4, '\u5df2\u5b8c\u6210'), (5, '\u9000\u6b3e\u7533\u8bf7\u4e2d'), (6, '\u9000\u6b3e\u4e2d'), (7, '\u9000\u6b3e\u6210\u529f')], default=0, verbose_name='\u72b6\u6001')),
                ('user', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='\u7528\u6237')),
            ],
            options={
                'verbose_name': '\u53d1\u5e03\u623f\u6e90\u8ba2\u5355',
                'verbose_name_plural': '\u53d1\u5e03\u623f\u6e90\u8ba2\u5355',
            },
        ),
        migrations.CreateModel(
            name='Infrastructure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_del', models.BooleanField(default=False, verbose_name='\u662f\u5426\u5220\u9664')),
                ('is_valid', models.BooleanField(default=True, verbose_name='\u662f\u5426\u53ef\u7528')),
                ('updated', models.DateTimeField(auto_now=True, null=True, verbose_name='\u66f4\u65b0\u65f6\u95f4')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('name', models.CharField(max_length=128, verbose_name='\u540d\u79f0')),
                ('order_no', models.IntegerField(default=0, verbose_name='\u6392\u5e8f\u53f7')),
                ('cover', models.CharField(blank=True, default='', max_length=1024, verbose_name='\u56fe\u7247')),
            ],
            options={
                'verbose_name': '\u57fa\u7840\u8bbe\u65bd',
                'verbose_name_plural': '\u57fa\u7840\u8bbe\u65bd',
            },
        ),
        migrations.CreateModel(
            name='JointVenture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_del', models.BooleanField(default=False, verbose_name='\u662f\u5426\u5220\u9664')),
                ('is_valid', models.BooleanField(default=True, verbose_name='\u662f\u5426\u53ef\u7528')),
                ('updated', models.DateTimeField(auto_now=True, null=True, verbose_name='\u66f4\u65b0\u65f6\u95f4')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('name', models.CharField(default='', max_length=128, verbose_name='\u540d\u79f0')),
                ('mobile', models.CharField(default='', max_length=128, verbose_name='\u7535\u8bdd')),
                ('address', models.CharField(default='', max_length=300, verbose_name='\u5730\u5740')),
                ('cover', models.CharField(default='', max_length=128, verbose_name='\u5934\u50cf')),
                ('intro', models.TextField(default='', verbose_name='\u7b80\u4ecb')),
                ('balance', models.FloatField(default=0, null=True, verbose_name='\u4f59\u989d')),
            ],
            options={
                'verbose_name': '\u5408\u4f5c\u4f01\u4e1a',
                'verbose_name_plural': '\u5408\u4f5c\u4f01\u4e1a',
            },
        ),
        migrations.CreateModel(
            name='JointVentureAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_del', models.BooleanField(default=False, verbose_name='\u662f\u5426\u5220\u9664')),
                ('is_valid', models.BooleanField(default=True, verbose_name='\u662f\u5426\u53ef\u7528')),
                ('updated', models.DateTimeField(auto_now=True, null=True, verbose_name='\u66f4\u65b0\u65f6\u95f4')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('joint_venture', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='web.JointVenture', verbose_name='\u5408\u4f5c\u4f01\u4e1a')),
            ],
            options={
                'verbose_name': '\u5408\u4f5c\u4f01\u4e1a/\u7ba1\u7406\u5458\u8d26\u53f7',
                'verbose_name_plural': '\u5408\u4f5c\u4f01\u4e1a/\u7ba1\u7406\u5458\u8d26\u53f7',
            },
        ),
        migrations.CreateModel(
            name='Permissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_del', models.BooleanField(default=False, verbose_name='\u662f\u5426\u5220\u9664')),
                ('is_valid', models.BooleanField(default=True, verbose_name='\u662f\u5426\u53ef\u7528')),
                ('updated', models.DateTimeField(auto_now=True, null=True, verbose_name='\u66f4\u65b0\u65f6\u95f4')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('name', models.CharField(max_length=128, verbose_name='\u540d\u79f0')),
                ('menu_str', models.TextField(blank=True, default='', verbose_name='\u83dc\u5355id')),
                ('menu_name_str', models.TextField(blank=True, default='', verbose_name='\u83dc\u5355\u540d\u79f0')),
            ],
            options={
                'verbose_name': '\u6743\u9650\u7ec4',
                'verbose_name_plural': '\u6743\u9650\u7ec4',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_del', models.BooleanField(default=False, verbose_name='\u662f\u5426\u5220\u9664')),
                ('is_valid', models.BooleanField(default=True, verbose_name='\u662f\u5426\u53ef\u7528')),
                ('updated', models.DateTimeField(auto_now=True, null=True, verbose_name='\u66f4\u65b0\u65f6\u95f4')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('email', models.CharField(blank=True, default='', max_length=128, verbose_name='\u90ae\u7bb1')),
                ('user_name', models.CharField(default='', max_length=128, verbose_name='\u59d3\u540d')),
                ('nickname', models.CharField(default='', max_length=128, verbose_name='\u6635\u79f0')),
                ('password', models.CharField(blank=True, default='', max_length=255, verbose_name='\u5bc6\u7801')),
                ('jwt_token', models.TextField(blank=True, default='', null=True, verbose_name='jwt_token')),
                ('openid', models.CharField(default='', max_length=255, verbose_name='openid')),
                ('user_login_type', models.IntegerField(choices=[(1, '\u624b\u673a\u7528\u6237'), (2, '\u5fae\u4fe1\u7528\u6237'), (3, '\u5fae\u535a\u7528\u6237'), (4, 'qq')], default=1, verbose_name='\u7528\u6237\u6ce8\u518c\u7c7b\u578b')),
                ('gender', models.IntegerField(choices=[(1, '\u7537'), (2, '\u5973')], default=1, verbose_name='\u6027\u522b')),
                ('age', models.IntegerField(default=0, verbose_name='\u5e74\u9f84')),
                ('id_card', models.CharField(blank=True, default='', max_length=128, verbose_name='\u8eab\u4efd\u8bc1\u4fe1\u606f')),
                ('id_card_status', models.IntegerField(choices=[(0, '\u672a\u8ba4\u8bc1'), (1, '\u5df2\u8ba4\u8bc1')], default=1, verbose_name='\u8eab\u4efd\u8ba4\u8bc1\u4fe1\u606f')),
                ('bank_acount', models.CharField(blank=True, default='', max_length=128, verbose_name='\u94f6\u884c\u5361\u4fe1\u606f')),
                ('id_card_picture', models.CharField(blank=True, default='', max_length=255, verbose_name='\u8eab\u4efd\u8bc1')),
                ('mobile', models.CharField(blank=True, default='', max_length=16, verbose_name='\u624b\u673a')),
                ('avatar', models.CharField(blank=True, default='', max_length=300, null=True, verbose_name='\u5934\u50cf')),
                ('birbath', models.DateField(default=datetime.date.today, verbose_name='\u751f\u65e5')),
                ('wx_unionid', models.CharField(blank=True, default='', max_length=300, verbose_name='\u5fae\u4fe1id')),
                ('weibo_uid', models.CharField(blank=True, default='', max_length=300, verbose_name='\u5fae\u535aid')),
                ('qq_uid', models.CharField(blank=True, default='', max_length=300, verbose_name='qqid')),
                ('promo_code', models.CharField(blank=True, default='', max_length=300, verbose_name='\u52a8\u6001\u7801')),
                ('employe', models.CharField(blank=True, default='', max_length=300, verbose_name='\u5de5\u4f5c\u5355\u4f4d')),
                ('user', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='\u7528\u6237')),
            ],
            options={
                'verbose_name': '\u7528\u6237\u4fe1\u606f',
                'verbose_name_plural': '\u7528\u6237\u4fe1\u606f',
            },
        ),
        migrations.CreateModel(
            name='RentHouse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_del', models.BooleanField(default=False, verbose_name='\u662f\u5426\u5220\u9664')),
                ('is_valid', models.BooleanField(default=True, verbose_name='\u662f\u5426\u53ef\u7528')),
                ('updated', models.DateTimeField(auto_now=True, null=True, verbose_name='\u66f4\u65b0\u65f6\u95f4')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('rent', models.IntegerField(choices=[(0, '0-500'), (1, '500-1000'), (2, '1000-1500'), (3, '1500-2000'), (4, '2000-2500'), (5, '2500-3000'), (6, '3000-3500'), (7, '3500-4000'), (8, '4000\u4ee5\u4e0a'), (9, '\u4e0d\u9650')], default=0, verbose_name='\u79df\u91d1')),
                ('description', models.CharField(blank=True, default='', max_length=1024, verbose_name='\u8865\u5145\u8bf4\u660e')),
                ('province', models.CharField(blank=True, default='', max_length=32, null=True, verbose_name='\u7701')),
                ('city', models.CharField(blank=True, default='', max_length=32, null=True, verbose_name='\u5e02')),
                ('area', models.CharField(blank=True, default='', max_length=32, null=True, verbose_name='\u533a')),
                ('date', models.CharField(blank=True, default='', max_length=32, null=True, verbose_name='\u6700\u8fdf\u5165\u4f4f\u65e5\u671f')),
                ('lease', models.IntegerField(choices=[(0, '\u5408\u79df'), (1, '\u6574\u79df')], default=0, verbose_name='\u79df\u8d41\u65b9\u5f0f')),
                ('male_count', models.IntegerField(blank=True, choices=[(0, '1'), (1, '2'), (2, '3'), (3, '4')], default=0, null=True, verbose_name='\u7537\u6027\u4eba\u6570')),
                ('female_count', models.IntegerField(blank=True, choices=[(0, '1'), (1, '2'), (2, '3'), (3, '4')], default=0, null=True, verbose_name='\u5973\u6027\u4eba\u6570')),
                ('relationship', models.IntegerField(blank=True, choices=[(0, '\u670b\u53cb'), (1, '\u60c5\u4fa3'), (2, '\u540c\u5b66'), (3, '\u4eb2\u621a'), (4, '\u964c\u751f\u4eba'), (5, '\u5176\u4ed6')], default=0, null=True, verbose_name='\u5173\u7cfb')),
                ('total_count', models.IntegerField(blank=True, choices=[(0, '1'), (1, '2'), (2, '3'), (3, '4'), (4, '5'), (5, '6')], default=0, null=True, verbose_name='\u603b\u4eba\u6570')),
                ('accept', models.IntegerField(blank=True, choices=[(0, '\u767d\u9886'), (1, '\u5b66\u751f'), (2, '\u4e0d\u9650')], default=0, null=True, verbose_name='\u80fd\u63a5\u53d7\u7684\u5408\u79df\u5bf9\u8c61')),
                ('name', models.CharField(blank=True, default='', max_length=32, verbose_name='\u59d3\u540d')),
                ('phone', models.CharField(blank=True, default='', max_length=11, verbose_name='\u624b\u673a')),
                ('status', models.IntegerField(choices=[(0, ''), (1, '\u4e0b\u7ebf'), (2, '\u4e0a\u7ebf')], default=0, verbose_name='\u72b6\u6001')),
                ('audit_status', models.IntegerField(choices=[(0, '\u5f85\u5ba1\u6838'), (1, '\u5ba1\u6838\u4e0d\u901a\u8fc7'), (2, '\u5ba1\u6838\u901a\u8fc7')], default=0, verbose_name='\u5ba1\u6838\u72b6\u6001')),
                ('infrastructure', models.ManyToManyField(to='web.Infrastructure', verbose_name='\u57fa\u7840\u8bbe\u65bd')),
                ('user', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='\u7528\u6237')),
            ],
            options={
                'verbose_name': '\u6c42\u79df\u53d1\u5e03',
                'verbose_name_plural': '\u6c42\u79df\u53d1\u5e03',
            },
        ),
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_del', models.BooleanField(default=False, verbose_name='\u662f\u5426\u5220\u9664')),
                ('is_valid', models.BooleanField(default=True, verbose_name='\u662f\u5426\u53ef\u7528')),
                ('updated', models.DateTimeField(auto_now=True, null=True, verbose_name='\u66f4\u65b0\u65f6\u95f4')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('name', models.CharField(default='', max_length=100, verbose_name='\u5b57\u6bb5')),
                ('value', models.CharField(default='', max_length=100, verbose_name='\u503c')),
                ('code', models.CharField(default='', max_length=100, verbose_name='code')),
            ],
            options={
                'verbose_name': '\u914d\u7f6e',
                'verbose_name_plural': '\u914d\u7f6e',
            },
        ),
        migrations.CreateModel(
            name='Withdrawal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_del', models.BooleanField(default=False, verbose_name='\u662f\u5426\u5220\u9664')),
                ('is_valid', models.BooleanField(default=True, verbose_name='\u662f\u5426\u53ef\u7528')),
                ('updated', models.DateTimeField(auto_now=True, null=True, verbose_name='\u66f4\u65b0\u65f6\u95f4')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('money', models.FloatField(default=0, null=True, verbose_name='\u91d1\u989d')),
                ('reason', models.CharField(default='', max_length=300, verbose_name='\u7406\u7531')),
                ('status', models.IntegerField(choices=[(0, '\u672a\u5904\u7406'), (1, '\u901a\u8fc7'), (2, '\u4e0d\u901a\u8fc7')], default=0, verbose_name='\u72b6\u6001')),
                ('join_tventure', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='web.JointVenture', verbose_name='\u5408\u4f5c\u4f01\u4e1a')),
            ],
            options={
                'verbose_name': '\u63d0\u73b0',
                'verbose_name_plural': '\u63d0\u73b0',
            },
        ),
        migrations.CreateModel(
            name='Words',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_del', models.BooleanField(default=False, verbose_name='\u662f\u5426\u5220\u9664')),
                ('is_valid', models.BooleanField(default=True, verbose_name='\u662f\u5426\u53ef\u7528')),
                ('updated', models.DateTimeField(auto_now=True, null=True, verbose_name='\u66f4\u65b0\u65f6\u95f4')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('content', models.TextField(blank=True, default='', verbose_name='\u5185\u5bb9')),
            ],
            options={
                'verbose_name': '\u654f\u611f\u8bcd',
                'verbose_name_plural': '\u654f\u611f\u8bcd',
            },
        ),
        migrations.AddField(
            model_name='jointventureaccount',
            name='permissions',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='web.Permissions', verbose_name='\u6240\u5c5e\u6743\u9650\u7ec4'),
        ),
        migrations.AddField(
            model_name='jointventureaccount',
            name='user',
            field=models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='\u7528\u6237'),
        ),
        migrations.AddField(
            model_name='housingresources',
            name='infrastructure',
            field=models.ManyToManyField(to='web.Infrastructure', verbose_name='\u57fa\u7840\u8bbe\u65bd'),
        ),
        migrations.AddField(
            model_name='housingresources',
            name='user',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='\u7528\u6237'),
        ),
        migrations.AddField(
            model_name='housingpicture',
            name='housing_resources',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='web.HousingResources', verbose_name='\u623f\u6e90'),
        ),
        migrations.AddField(
            model_name='bedroom',
            name='housing_resources',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='web.HousingResources', verbose_name='\u623f\u6e90'),
        ),
    ]
