# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oh', '0009_auto_20150928_1325'),
    ]

    operations = [
        migrations.AddField(
            model_name='openhardware',
            name='attachments',
            field=models.ManyToManyField(to='oh.OpenHardwareAttachment'),
        ),
    ]
