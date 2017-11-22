# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-19 17:10
from __future__ import unicode_literals

import DjangoUeditor.models
import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='标题')),
                ('image', models.ImageField(upload_to='content/', verbose_name='图片')),
                ('resouce', models.CharField(max_length=20, verbose_name='来源')),
                ('see_num', models.IntegerField(default=1, verbose_name='阅读人数')),
                ('see_unkown_num', models.IntegerField(default=0, verbose_name='未登录查看人数')),
                ('content', DjangoUeditor.models.UEditorField(default='', verbose_name='内容')),
                ('fav_nums', models.IntegerField(default=0, verbose_name='点赞数')),
                ('tag', models.CharField(max_length=20, verbose_name='课程标签')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '文章',
                'verbose_name_plural': '文章',
            },
        ),
        migrations.CreateModel(
            name='Catagory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='栏目')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '文章',
                'verbose_name_plural': '文章',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='column',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='acticle.Catagory', verbose_name='栏目'),
        ),
    ]
