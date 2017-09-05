# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-02 00:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default='test_<function now at 0x101fa10d0>', max_length=100, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default='slug_<function now at 0x101fa10d0>', max_length=100, unique=True),
            preserve_default=False,
        ),
    ]