# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-11 05:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0004_auto_20161110_0855'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='following',
            unique_together=set([('follower', 'followee')]),
        ),
    ]
