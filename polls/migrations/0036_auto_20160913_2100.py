# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-09-13 15:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0035_delete_question'),
    ]

    operations = [
        migrations.AlterField(
            model_name='global',
            name='sessionid',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='password',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='conpassword',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='password',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]