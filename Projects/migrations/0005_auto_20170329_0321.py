# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-29 03:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Projects', '0004_auto_20170328_1702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='language',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='projectpage',
            name='images',
            field=models.TextField(blank=True, null=True),
        ),
    ]