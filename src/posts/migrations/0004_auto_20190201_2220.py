# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-02-01 22:20
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20190201_2159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publish',
            field=models.DateField(default=datetime.datetime(2019, 2, 1, 22, 19, 30, 537635, tzinfo=utc)),
        ),
    ]