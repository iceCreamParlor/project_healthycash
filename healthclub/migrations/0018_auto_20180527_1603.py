# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-27 16:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('healthclub', '0017_auto_20180526_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='healthclub',
            name='price1',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='healthclub',
            name='price12',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='healthclub',
            name='price2',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='healthclub',
            name='price3',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='healthclub',
            name='price6',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]