# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-30 07:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EKSite', '0003_auto_20170830_0459'),
    ]

    operations = [
        migrations.AddField(
            model_name='featuredheader',
            name='link',
            field=models.URLField(default='https://ekletik.com'),
        ),
    ]