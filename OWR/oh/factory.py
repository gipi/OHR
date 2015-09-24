from __future__ import absolute_import
from .models import OpenHardware
import factory

class OpenHardwareFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = OpenHardware