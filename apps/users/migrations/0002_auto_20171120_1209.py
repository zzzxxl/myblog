# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-20 12:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='banner',
            options={'verbose_name': '轮播图', 'verbose_name_plural': '轮播图'},
        ),
        migrations.AlterModelOptions(
            name='friendweb',
            options={'verbose_name': '友链', 'verbose_name_plural': '友链'},
        ),
        migrations.AlterField(
            model_name='banner',
            name='title',
            field=models.CharField(max_length=50, verbose_name='标题'),
        ),
        migrations.AlterField(
            model_name='friendweb',
            name='title',
            field=models.CharField(max_length=10, verbose_name='友链'),
        ),
    ]
