# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-08-09 07:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_customer_order_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='house_product',
            name='sKU',
        ),
    ]
