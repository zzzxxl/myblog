# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-20 12:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acticle', '0002_auto_20171120_1025'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='brief',
            field=models.CharField(default='', max_length=500, verbose_name='简介'),
        ),
    ]
