# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-16 16:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0014_auto_20180516_1543'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='password',
        ),
    ]
