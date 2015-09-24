from __future__ import absolute_import
from .models import User
import factory


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
        django_get_or_create = ('username',)


    username = factory.Sequence(lambda n: 'User {0}'.format(n))
    # http://stackoverflow.com/questions/15616277/how-can-you-create-an-admin-user-with-factory-boy
    password = factory.PostGenerationMethodCall('set_password', 'password')
