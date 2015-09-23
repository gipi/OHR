# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oh', '0002_auto_20150923_1428'),
    ]

    operations = [
        migrations.AddField(
            model_name='openhardware',
            name='layout',
            field=models.FileField(default='whatever', upload_to=None),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='openhardware',
            name='schematics',
            field=models.FileField(upload_to=None),
        ),
    ]
