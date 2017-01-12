# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-09-12 20:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0033_auto_20160911_0058'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='global',
            name='is_loggedin',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='interest1',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='interest2',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='interest3',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='interest4',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='interest5',
        ),
        migrations.AddField(
            model_name='users',
            name='name',
            field=models.CharField(default='none', max_length=200),
        ),
    ]
