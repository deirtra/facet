# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2019-05-13 00:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('editorial', '0090_auto_20190512_1558'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organizationdiscoveryprofile',
            name='platforms',
        ),
        migrations.AddField(
            model_name='organizationdiscoveryprofile',
            name='platform_cable_tv',
            field=models.BooleanField(default=False, help_text=b'Organization airs on cable television.'),
        ),
        migrations.AddField(
            model_name='organizationdiscoveryprofile',
            name='platform_network_tv',
            field=models.BooleanField(default=False, help_text=b'Organization airs on network television.'),
        ),
        migrations.AddField(
            model_name='organizationdiscoveryprofile',
            name='platform_newsletter',
            field=models.BooleanField(default=False, help_text=b'Organization publishes newsletters.'),
        ),
        migrations.AddField(
            model_name='organizationdiscoveryprofile',
            name='platform_online',
            field=models.BooleanField(default=False, help_text=b'Organization publishes online.'),
        ),
        migrations.AddField(
            model_name='organizationdiscoveryprofile',
            name='platform_podcast',
            field=models.BooleanField(default=False, help_text=b'Organization produces podcasts.'),
        ),
        migrations.AddField(
            model_name='organizationdiscoveryprofile',
            name='platform_print',
            field=models.BooleanField(default=False, help_text=b'Organization publishes in print.'),
        ),
        migrations.AddField(
            model_name='organizationdiscoveryprofile',
            name='platform_radio',
            field=models.BooleanField(default=False, help_text=b'Organization airs on radio.'),
        ),
        migrations.AddField(
            model_name='organizationdiscoveryprofile',
            name='platform_social',
            field=models.BooleanField(default=False, help_text=b'Organization publishes content on social platforms.'),
        ),
        migrations.AddField(
            model_name='organizationdiscoveryprofile',
            name='platform_streaming_video',
            field=models.BooleanField(default=False, help_text=b'Organization content airs on streaming video.'),
        ),
    ]
