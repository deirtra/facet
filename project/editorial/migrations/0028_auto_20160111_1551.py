# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.contrib.postgres.fields


class Migration(migrations.Migration):

    dependencies = [
        ('editorial', '0027_networknote_organizationnote'),
    ]

    operations = [
        migrations.AlterField(
            model_name='networknote',
            name='keywords',
            field=django.contrib.postgres.fields.ArrayField(default=list, help_text=b'List of keywords for note search.', size=None, base_field=models.CharField(max_length=100), blank=True),
        ),
        migrations.AlterField(
            model_name='organizationnote',
            name='keywords',
            field=django.contrib.postgres.fields.ArrayField(default=list, help_text=b'List of keywords for note search.', size=None, base_field=models.CharField(max_length=100), blank=True),
        ),
        migrations.AlterField(
            model_name='seriesnote',
            name='series',
            field=models.ForeignKey(related_name='seriesnote', to='editorial.Series'),
        ),
        migrations.AlterField(
            model_name='usernote',
            name='keywords',
            field=django.contrib.postgres.fields.ArrayField(default=list, help_text=b'List of keywords for search.', size=None, base_field=models.CharField(max_length=100), blank=True),
        ),
    ]
