# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-30 14:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EKSite', '0004_featuredheader_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='doc',
            name='summary',
            field=models.TextField(blank=True, max_length=100),
        ),
    ]