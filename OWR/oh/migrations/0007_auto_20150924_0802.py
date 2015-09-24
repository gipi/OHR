# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import OWR.oh.models


class Migration(migrations.Migration):

    dependencies = [
        ('oh', '0006_auto_20150924_0800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='openhardware',
            name='layout',
            field=models.FileField(upload_to=OWR.oh.models.resolve_upload_path_layout),
        ),
        migrations.AlterField(
            model_name='openhardware',
            name='schematics',
            field=models.FileField(upload_to=OWR.oh.models.resolve_upload_path_schematics),
        ),
    ]
