# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import OWR.oh.models


class Migration(migrations.Migration):

    dependencies = [
        ('oh', '0010_openhardware_attachments'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='openhardware',
            name='attachments',
        ),
        migrations.AddField(
            model_name='openhardware',
            name='slug',
            field=models.SlugField(default='miao', unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='openhardware',
            name='image',
            field=models.ImageField(upload_to=OWR.oh.models.upload_to_resolver_for_image),
        ),
    ]
