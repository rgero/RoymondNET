# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-29 18:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Projects', '0006_projectpage_related_projects'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectpage',
            name='related_projects',
            field=models.ManyToManyField(blank=True, to='Projects.ProjectPage'),
        ),
    ]