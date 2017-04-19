# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-21 04:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_otherif'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otherif',
            name='name',
            field=models.CharField(default='***', max_length=20, verbose_name='姓名'),
        ),
        migrations.AlterField(
            model_name='otherif',
            name='numb',
            field=models.CharField(default='***', max_length=20, verbose_name='工号'),
        ),
        migrations.AlterField(
            model_name='otherif',
            name='phone',
            field=models.CharField(default='***', max_length=20, verbose_name='电话'),
        ),
        migrations.AlterField(
            model_name='otherif',
            name='service',
            field=models.CharField(default='***', max_length=200, verbose_name='负责业务'),
        ),
    ]
