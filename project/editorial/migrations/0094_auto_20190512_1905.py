# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2019-05-13 02:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('editorial', '0093_auto_20190512_1852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organizationpublicprofile',
            name='org_structure',
            field=models.CharField(blank=True, choices=[(b'Nonprofit', b'Nonprofit'), (b'For profit', b'For profit'), (b'Other', b'Other')], help_text=b'Financial structure of the organization.', max_length=50),
        ),
    ]
