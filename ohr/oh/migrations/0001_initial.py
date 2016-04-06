# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import oh.models
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        ('licensing', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='OpenHardware',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('short_description', models.CharField(max_length=150)),
                ('url', models.URLField(help_text='Main site')),
                ('image', models.ImageField(upload_to=oh.models.upload_to_resolver_for_image)),
                ('slug', models.SlugField(unique=True)),
                ('tags', taggit.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', help_text='A comma-separated list of tags.', verbose_name='Tags')),
            ],
        ),
        migrations.CreateModel(
            name='OpenHardwareAttachment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(max_length=100, choices=[(b'schematics', b'schematics'), (b'layout', b'layout')])),
                ('file', models.FileField(upload_to=oh.models.upload_to_resolver)),
                ('description', models.CharField(help_text='Indicate for example what program can edit it', max_length=100)),
                ('license', models.ForeignKey(to='licensing.License')),
                ('oh', models.ForeignKey(to='oh.OpenHardware')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OpenHardwareLike',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('oh', models.ForeignKey(to='oh.OpenHardware')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
