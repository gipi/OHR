# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import OWR.oh.models


class Migration(migrations.Migration):

    dependencies = [
        ('oh', '0007_auto_20150924_0802'),
    ]

    operations = [
        migrations.CreateModel(
            name='OpenHardwareAttachment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(max_length=100, choices=[(b'schematics', b'schematics'), (b'layout', b'layout')])),
                ('file', models.FileField(upload_to=OWR.oh.models.upload_to_resolver)),
                ('description', models.CharField(help_text='Indicate for example what program can edit it', max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='openhardware',
            name='description',
        ),
        migrations.RemoveField(
            model_name='openhardware',
            name='image',
        ),
        migrations.RemoveField(
            model_name='openhardware',
            name='layout',
        ),
        migrations.RemoveField(
            model_name='openhardware',
            name='schematics',
        ),
        migrations.AddField(
            model_name='openhardwareattachment',
            name='oh',
            field=models.ForeignKey(to='oh.OpenHardware'),
        ),
        migrations.AddField(
            model_name='openhardware',
            name='attachments',
            field=models.ManyToManyField(to='oh.OpenHardwareAttachment'),
        ),
    ]
