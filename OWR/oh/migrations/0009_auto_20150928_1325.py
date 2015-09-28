# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import OWR.oh.models


class Migration(migrations.Migration):

    dependencies = [
        ('oh', '0008_auto_20150928_1321'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='openhardware',
            name='attachments',
        ),
        migrations.AddField(
            model_name='openhardware',
            name='image',
            field=models.ImageField(default='miao', upload_to=OWR.oh.models.resolve_upload_path_image),
            preserve_default=False,
        ),
    ]
