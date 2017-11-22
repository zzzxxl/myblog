# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-21 15:35
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0003_auto_20171119_1725'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': '评论', 'verbose_name_plural': '评论'},
        ),
        migrations.AlterModelOptions(
            name='userfav',
            options={'verbose_name': '收藏', 'verbose_name_plural': '收藏'},
        ),
        migrations.AlterField(
            model_name='userfav',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='acticle.Article', verbose_name='被收藏文章'),
        ),
        migrations.AlterField(
            model_name='userfav',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='收藏用户'),
        ),
    ]
