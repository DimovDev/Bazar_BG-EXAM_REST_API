# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-27 20:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('all_product', '0006_auto_20181025_0852'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='slug',
        ),
        migrations.AddField(
            model_name='location',
            name='image',
            field=models.ImageField(blank=True, upload_to='location/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='product',
            name='phone_number',
            field=models.CharField(blank=True, max_length=17),
        ),
    ]
