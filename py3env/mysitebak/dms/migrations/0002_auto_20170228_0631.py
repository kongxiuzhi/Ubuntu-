# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-28 06:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(default='example@example.com', max_length=254),
        ),
        migrations.AddField(
            model_name='user',
            name='job_number',
            field=models.CharField(default='0', max_length=10, verbose_name='工号'),
        ),
    ]
