# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-01 03:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_project'),
    ]

    operations = [
        migrations.CreateModel(
            name='result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('time', models.DateTimeField()),
                ('ps', models.CharField(max_length=10)),
                ('fail', models.CharField(max_length=10)),
                ('result', models.TextField()),
            ],
            options={
                'db_table': 'result',
            },
        ),
    ]
