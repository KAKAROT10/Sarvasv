# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-10 15:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0010_auto_20160510_1929'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='interest2',
            new_name='nterest2',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='interest3',
            new_name='nterest3',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='interest4',
            new_name='nterest4',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='interest5',
            new_name='nterest5',
        ),
    ]
