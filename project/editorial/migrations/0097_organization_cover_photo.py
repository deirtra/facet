# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2019-05-15 23:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('editorial', '0096_auto_20190514_2128'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='cover_photo',
            field=models.ImageField(blank=True, upload_to=b'org_cover'),
        ),
    ]
