# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-11-07 23:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plato', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plato',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='photo/'),
        ),
    ]
