# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-10 07:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=250)),
                ('pub_date', models.DateField()),
                ('content', models.TextField()),
                ('images', models.ImageField(upload_to='')),
            ],
        ),
    ]
