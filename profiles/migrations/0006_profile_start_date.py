# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-06 20:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_profile_expire_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='start_date',
            field=models.DateTimeField(null=True),
        ),
    ]