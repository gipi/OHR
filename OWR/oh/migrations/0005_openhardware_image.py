# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oh', '0004_auto_20150923_1516'),
    ]

    operations = [
        migrations.AddField(
            model_name='openhardware',
            name='image',
            field=models.ImageField(default='foobar', upload_to=b''),
            preserve_default=False,
        ),
    ]
