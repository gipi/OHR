# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import OWR.oh.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('oh', '0005_openhardware_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='OpenHardwareLike',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.AlterField(
            model_name='openhardware',
            name='image',
            field=models.ImageField(upload_to=OWR.oh.models.resolve_upload_path_image),
        ),
        migrations.AlterField(
            model_name='openhardware',
            name='layout',
            field=models.FileField(upload_to=OWR.oh.models.resolve_upload_path_image),
        ),
        migrations.AlterField(
            model_name='openhardware',
            name='schematics',
            field=models.FileField(upload_to=OWR.oh.models.resolve_upload_path_image),
        ),
        migrations.AddField(
            model_name='openhardwarelike',
            name='oh',
            field=models.ForeignKey(to='oh.OpenHardware'),
        ),
        migrations.AddField(
            model_name='openhardwarelike',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
