# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('licensing', '__first__'),
        ('oh', '0011_auto_20150928_2010'),
    ]

    operations = [
        migrations.AddField(
            model_name='openhardwareattachment',
            name='license',
            field=models.ForeignKey(default=1, to='licensing.License'),
            preserve_default=False,
        ),
    ]
