# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-28 05:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hexColor', models.CharField(max_length=7)),
            ],
        ),
        migrations.CreateModel(
            name='Doc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=45)),
                ('content', models.TextField()),
                ('publishedDate', models.DateTimeField()),
                ('updatedDate', models.DateTimeField()),
                ('programmingLanguages', models.CharField(choices=[('rb', 'Ruby'), ('py', 'Python'), ('sh', 'ShellScript'), ('c', 'C'), ('cpp', 'C++'), ('java', 'Java'), ('ru', 'Rust'), ('swift', 'Swift'), ('m', 'Objective-C'), ('html', 'HTML'), ('css', 'CSS'), ('js', 'JavaScript'), ('r', 'R')], default='py', max_length=5)),
                ('language', models.CharField(choices=[('en', 'English'), ('es', 'Español'), ('fr', 'Français'), ('it', 'Italiano'), ('pt', 'Português'), ('ro', 'Roumain')], default='pt', max_length=2)),
                ('slug', models.SlugField(unique=True)),
                ('status', models.CharField(choices=[('d', 'Draft'), ('p', 'Published')], default='d', max_length=1)),
            ],
            options={
                'verbose_name_plural': 'EKSite Docs',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('photo', models.ImageField(max_length=45, upload_to='Uploads/profiles/')),
                ('bio', models.TextField(max_length=100)),
                ('github_username', models.CharField(max_length=30)),
                ('status', models.CharField(choices=[('d', 'Draft'), ('p', 'Published')], default='d', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(max_length=45, upload_to='Uploads/projects/')),
            ],
        ),
        migrations.CreateModel(
            name='PortfolioProject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=15)),
                ('type', models.CharField(max_length=15)),
                ('client', models.CharField(max_length=15)),
                ('description', models.TextField(max_length=500)),
                ('details', models.CharField(blank=True, max_length=30)),
                ('artwork', models.ImageField(max_length=45, upload_to='Uploads/projects/')),
                ('featured', models.BooleanField(default=False)),
                ('publishedDate', models.DateTimeField()),
                ('slug', models.SlugField(unique=True)),
                ('status', models.CharField(choices=[('d', 'Draft'), ('p', 'Published')], default='d', max_length=1)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EKSite.Person')),
            ],
            options={
                'verbose_name_plural': 'Portfolio',
            },
        ),
        migrations.AddField(
            model_name='photo',
            name='projectName',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EKSite.PortfolioProject'),
        ),
        migrations.AddField(
            model_name='doc',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EKSite.Person'),
        ),
        migrations.AddField(
            model_name='color',
            name='projectName',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EKSite.PortfolioProject'),
        ),
    ]