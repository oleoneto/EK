# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-23 22:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EKSite', '0021_auto_20171123_1744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audio',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]