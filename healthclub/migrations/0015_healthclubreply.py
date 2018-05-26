# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-26 14:11
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('healthclub', '0014_auto_20180526_1218'),
    ]

    operations = [
        migrations.CreateModel(
            name='HealthClubReply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reply', models.CharField(max_length=300)),
                ('healthclub', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='healthclub.HealthClub')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
