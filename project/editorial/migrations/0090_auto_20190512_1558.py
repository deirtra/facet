# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2019-05-12 22:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('editorial', '0089_auto_20190227_1903'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrganizationDiscoveryProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('org_structure', models.CharField(choices=[(b'Nonprofit', b'Nonprofit'), (b'For profit', b'For profit'), (b'Other', b'Other')], help_text=b'Financial structure of the organization.', max_length=50)),
                ('platforms', models.CharField(blank=True, choices=[(b'Print', b'Print'), (b'Online', b'Online'), (b'Social Platform', b'Social Platform'), (b'Network TV', b'Network TV'), (b'Cable TV', b'Cable TV'), (b'Radio', b'Radio'), (b'Podcast', b'Podcast'), (b'Newsletter', b'Newsletter'), (b'Streaming Video', b'Streaming Video')], help_text=b'Distribution platforms.', max_length=500)),
                ('primary_audience', models.CharField(blank=True, help_text=b'Is the audience geographic, topic or of a special community.', max_length=255)),
                ('ownership', models.CharField(blank=True, help_text=b'What is the ownership structure of the organization. What or who owns the organization.', max_length=255)),
                ('business_model', models.CharField(blank=True, help_text=b'What are the sources of support for the organization.', max_length=255)),
                ('unionized_workforce', models.CharField(blank=True, help_text=b'Is any part of the organization workforce unionized.', max_length=255)),
                ('diversity', models.TextField(blank=True, help_text=b'The makeup of the organization and any programs or efforts to help ensure diversity in staffing.')),
                ('special_skills', models.TextField(blank=True, help_text=b'Any special skills or strengths this newsroom has.')),
                ('good_partner', models.TextField(blank=True, help_text=b'What about this organization makes it a good collaborative partner.')),
                ('best_coverage', models.TextField(blank=True, help_text=b'What coverage has this organization been involved in that the newsroom is proud of.')),
                ('collab_experience', models.CharField(blank=True, help_text=b'Has the organization collaborated before and how often.', max_length=500)),
            ],
        ),
        migrations.AddField(
            model_name='organization',
            name='list_publicly',
            field=models.BooleanField(default=False, help_text=b'Whether the organization is listed publicly in discovery.'),
        ),
        migrations.AddField(
            model_name='organizationsubscription',
            name='partner_discovery',
            field=models.BooleanField(default=True, help_text=b'Base level subscription. Allows organization to be publicly listed for search as a potential collaborative partner. Allows org users to see other publicly listed orgs.'),
        ),
        migrations.AlterField(
            model_name='organizationsubscription',
            name='collaborations',
            field=models.BooleanField(default=False, help_text=b'The organization is using the account for base features of editorial workflow, project management and collaboration.'),
        ),
        migrations.AlterField(
            model_name='organizationsubscription',
            name='contractors',
            field=models.BooleanField(default=False, help_text=b'The organization is using the account to manage contractors.'),
        ),
        migrations.AlterField(
            model_name='organizationsubscription',
            name='organization',
            field=models.OneToOneField(help_text=b'Organization associated with this subscription if Org subscription type.', on_delete=django.db.models.deletion.CASCADE, to='editorial.Organization'),
        ),
        migrations.AddField(
            model_name='organizationdiscoveryprofile',
            name='organization',
            field=models.OneToOneField(help_text=b'Organization associated with this profile.', on_delete=django.db.models.deletion.CASCADE, to='editorial.Organization'),
        ),
    ]
