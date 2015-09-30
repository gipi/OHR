from __future__ import absolute_import
from .models import OpenHardware
import factory

class OpenHardwareFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = OpenHardware

    name = factory.Sequence(lambda n: 'name {0}'.format(n))
    slug = factory.Sequence(lambda n: 'slug-{0}'.format(n))