# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-01-10 04:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20200109_2010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitor',
            name='present',
            field=models.BooleanField(default=True),
        ),
    ]
