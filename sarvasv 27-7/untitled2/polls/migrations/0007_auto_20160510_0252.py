# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-09 21:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_auto_20160509_1534'),
    ]

    operations = [
        migrations.RenameField(
            model_name='global',
            old_name='session_id',
            new_name='sessionid',
        ),
    ]