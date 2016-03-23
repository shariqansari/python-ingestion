# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-23 17:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('deployments', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='datasourcetype',
            options={'verbose_name': 'Data Source Type'},
        ),
        migrations.AlterField(
            model_name='datasourcetype',
            name='abbr',
            field=models.CharField(max_length=3, verbose_name='Abbreviation'),
        ),
        migrations.AlterField(
            model_name='deployment',
            name='csv_file',
            field=models.FileField(blank=True, null=True, upload_to=b'', verbose_name='CSV File'),
        ),
        migrations.AlterField(
            model_name='deployment',
            name='data_source',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='deployments.DataSourceType', verbose_name='Data Source'),
        ),
    ]
