# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-20 21:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20170320_2003'),
    ]

    operations = [
        migrations.AddField(
            model_name='links',
            name='picurl',
            field=models.ImageField(blank=True, default='/media/link/default.png', null=True, upload_to='link/%Y/%m', verbose_name='图片路径'),
        ),
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Category', verbose_name='分类'),
        ),
    ]