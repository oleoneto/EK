# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-03 17:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EKSite', '0008_featuredheader_emoji'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='position',
            field=models.CharField(blank=True, max_length=45),
        ),
    ]