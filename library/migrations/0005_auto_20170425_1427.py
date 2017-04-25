# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-25 14:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0004_auto_20170425_1413'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='picture_url',
            field=models.ImageField(blank=True, null=True, upload_to='library/static/images/author/%Y%m%d%H%M%S'),
        ),
        migrations.AlterField(
            model_name='book',
            name='picture_url',
            field=models.ImageField(blank=True, null=True, upload_to='library/static/images/book/%Y%m%d%H%M%S'),
        ),
    ]
