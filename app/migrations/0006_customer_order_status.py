# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-08-07 21:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_requested_supply_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer_order',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
