# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-11 07:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='images',
            field=models.ImageField(upload_to='media/'),
        ),
    ]
