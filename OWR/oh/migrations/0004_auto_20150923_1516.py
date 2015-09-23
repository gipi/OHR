# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oh', '0003_auto_20150923_1501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='openhardware',
            name='layout',
            field=models.FileField(upload_to=b''),
        ),
        migrations.AlterField(
            model_name='openhardware',
            name='schematics',
            field=models.FileField(upload_to=b''),
        ),
    ]
