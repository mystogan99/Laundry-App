# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2019-07-14 07:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_product_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='email',
            field=models.CharField(default='', max_length=100),
        ),
    ]
