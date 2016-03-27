from __future__ import absolute_import
import json
import random

from django.test.client import RequestFactory
from django.core.urlresolvers import reverse
from django.contrib.auth.models import AnonymousUser
from django.core.exceptions import SuspiciousOperation, PermissionDenied
from django.test import Client, TestCase

from users.factory import UserFactory

from .models import OpenHardwareLike
from .views import like_set
from .factory import OpenHardwareFactory


class OpenHardwareViewTests(TestCase):
    BATCH_NUMBER = 10
    def setUp(self):
        self.client = Client()
        self.factory = RequestFactory()
        # we are creating two users (1 normal, 1 superuser)
        self.user  = UserFactory()
        self.admin = UserFactory(username='admin', is_superuser=True, is_staff=True)
        # and a bunch of openhardware instances
        self.ohs = OpenHardwareFactory.create_batch(self.BATCH_NUMBER)

    def test_like_add_not_logged(self):
        count_start = OpenHardwareLike.objects.count()

        exception = False
        response = None

        # this is not logged
        request = self.factory.post(reverse('oh:like_set'), data=json.dumps({'id': 1}), content_type='text/javascript')
        request.user = AnonymousUser()
        try:
            response = like_set(request)
        except PermissionDenied as e:
            exception = True
            # TODO: test error parameters
            #js = json.loads(response.body)

        count_final = OpenHardwareLike.objects.count()

        self.assertEqual(exception, True, 'An exception must raise if the user is not logged')
        self.assertEqual(count_start, count_final)

    def test_like_add_logged(self):
        idx = random.randrange(0, self.BATCH_NUMBER)
        count_start = OpenHardwareLike.objects.count()

        # this is logged
        request = self.factory.post(reverse('oh:like_set'), data=json.dumps({'id': self.ohs[idx].pk, 'action': 'set'}), content_type='text/javascript')
        request.user = self.user
        response = like_set(request)

        count_final = OpenHardwareLike.objects.count()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(count_start + 1, count_final)

    def test_like_with_malformed_json(self):
        count_start = OpenHardwareLike.objects.count()
        exception = False

        # this is logged
        request = self.factory.post(reverse('oh:like_set'), data=json.dumps({'id': 1, 'action': 'foobar'}), content_type='text/javascript')
        request.user = self.user

        try:
            response = like_set(request)
        except SuspiciousOperation as e:
            exception = True
            # TODO: test error parameters
            #js = json.loads(response.body)

        count_final = OpenHardwareLike.objects.count()

        self.assertEqual(exception, True)
        self.assertEqual(count_start, count_final)


    def test_remove_like(self):
        deal_to_test = self.ohs[0]
        OpenHardwareLike.objects.create(oh=deal_to_test, user=self.user)
        count_start = OpenHardwareLike.objects.count()

        # this is logged
        request = self.factory.post(reverse('oh:like_set'), data=json.dumps({'id': deal_to_test.pk, 'action': 'unset'}), content_type='text/javascript')
        request.user = self.user
        response = like_set(request)

        count_final = OpenHardwareLike.objects.count()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(count_start - 1, count_final)

        self.assertEqual(json.loads(response.content), {'action': 'unset', 'status': 'ok'})

    def test_index(self):
        '''We check for stuffs should be in home page.'''
        response = self.client.get(reverse('home'))

        self.assertEqual(response.status_code, 200)

        self.assertTrue(self.client.login(username=self.user.username, password='password'))
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_users_list(self):
        '''We want a list without superuser listed'''
        self.assertTrue(self.client.login(username=self.user.username, password='password'))
        response = self.client.get(reverse('users:list'))

        self.assertEqual(response.status_code, 200)

        obtained_qs = response.context['object_list']
        desired_qs  = [self.user.username,]

        self.assertQuerysetEqual(obtained_qs, desired_qs, transform=lambda x:x.username, ordered=False)

    def test_admin(self):
        self.assertTrue(self.client.login(username=self.admin.username, password='password'))

        url = reverse('admin:oh_openhardware_add')

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
