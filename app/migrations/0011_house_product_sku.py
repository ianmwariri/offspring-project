# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-08-09 08:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_remove_customer_order_sku'),
    ]

    operations = [
        migrations.AddField(
            model_name='house_product',
            name='sKU',
            field=models.CharField(default='h', max_length=40),
            preserve_default=False,
        ),
    ]
