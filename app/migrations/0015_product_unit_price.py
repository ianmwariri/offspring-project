# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-07-26 21:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_auto_20190726_1739'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='unit_price',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
