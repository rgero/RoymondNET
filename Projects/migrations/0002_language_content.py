# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-28 20:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='language',
            name='content',
            field=models.TextField(null=True),
        ),
    ]
