# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-20 08:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='文章题目')),
                ('slug', models.SlugField(max_length=250, unique_for_date='publish', verbose_name='url')),
                ('author', models.CharField(max_length=20, verbose_name='作者')),
                ('body', models.TextField(verbose_name='文章内容')),
                ('publish', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创作时间')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('草稿', '草稿'), ('发表', '发表')], default='草稿', max_length=10, verbose_name='是否发表')),
            ],
            options={
                'ordering': ('-publish',),
            },
        ),
        migrations.CreateModel(
            name='StaffIf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='姓名')),
                ('phone', models.CharField(max_length=20, verbose_name='电话号码')),
                ('mail', models.EmailField(max_length=254, verbose_name='邮箱')),
                ('incomp', models.CharField(choices=[('上班', '上班'), ('休息', '休息')], max_length=2, verbose_name='今天是否上班')),
                ('service', models.TextField(verbose_name='负责业务')),
                ('work', models.TextField(verbose_name='工作安排')),
            ],
            options={
                'db_table': 'EmInformation',
            },
        ),
    ]
