# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import OWR.oh.models


class Migration(migrations.Migration):

    dependencies = [
        ('oh', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='openhardware',
            name='schematics',
            field=models.FileField(default='/path/', upload_to=OWR.oh.models.resolve_upload_path),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='openhardware',
            name='url',
            field=models.URLField(default='http://example.com', help_text='Main site'),
            preserve_default=False,
        ),
    ]
