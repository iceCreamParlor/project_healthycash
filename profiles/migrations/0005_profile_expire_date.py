# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-06 20:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_auto_20180506_0117'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='expire_date',
            field=models.DateTimeField(null=True),
        ),
    ]
