# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2019-02-28 03:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('editorial', '0088_auto_20180411_2004'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='series',
            name='collaborate_with',
        ),
        migrations.RemoveField(
            model_name='series',
            name='discussion',
        ),
        migrations.RemoveField(
            model_name='series',
            name='notes',
        ),
        migrations.RemoveField(
            model_name='series',
            name='organization',
        ),
        migrations.RemoveField(
            model_name='series',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='series',
            name='simple_audio_assets',
        ),
        migrations.RemoveField(
            model_name='series',
            name='simple_document_assets',
        ),
        migrations.RemoveField(
            model_name='series',
            name='simple_image_assets',
        ),
        migrations.RemoveField(
            model_name='series',
            name='simple_video_assets',
        ),
        migrations.RemoveField(
            model_name='series',
            name='team',
        ),
        migrations.RemoveField(
            model_name='seriescopydetail',
            name='original_org',
        ),
        migrations.RemoveField(
            model_name='seriescopydetail',
            name='original_series',
        ),
        migrations.RemoveField(
            model_name='seriescopydetail',
            name='partner',
        ),
        migrations.RemoveField(
            model_name='seriescopydetail',
            name='partner_series',
        ),
        migrations.RemoveField(
            model_name='event',
            name='series',
        ),
        migrations.RemoveField(
            model_name='story',
            name='series',
        ),
        migrations.RemoveField(
            model_name='task',
            name='series',
        ),
        migrations.AlterField(
            model_name='discussion',
            name='discussion_type',
            field=models.CharField(choices=[(b'ORG', b'Organization Conversation'), (b'NET', b'Network Conversation'), (b'PRI', b'Private Conversation'), (b'PRO', b'Project Conversation'), (b'STO', b'Story Conversation'), (b'F', b'Facet Conversation'), (b'TSK', b'Task Conversation'), (b'EV', b'Event Conversation')], help_text=b'What kind of discussion is it.', max_length=25),
        ),
        migrations.AlterField(
            model_name='note',
            name='note_type',
            field=models.CharField(choices=[(b'ORG', b'Organization'), (b'NET', b'Network'), (b'USER', b'User'), (b'PRO', b'Project'), (b'STO', b'Story'), (b'TSK', b'Task'), (b'EV', b'Event')], help_text=b'The kind of object this note is for.', max_length=25),
        ),
        migrations.AlterField(
            model_name='story',
            name='collaborate_with',
            field=models.ManyToManyField(blank=True, help_text=b'Organization ids that a story is open to collaboration with.', related_name='story_collaborated_with_organization', to='editorial.Organization'),
        ),
        migrations.DeleteModel(
            name='Series',
        ),
        migrations.DeleteModel(
            name='SeriesCopyDetail',
        ),
    ]
