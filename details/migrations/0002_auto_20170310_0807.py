# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-10 08:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetails',
            name='fname',
            field=models.CharField(max_length=16, null=True),
        ),
    ]
