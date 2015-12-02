from __future__ import absolute_import
import json
import random

from unittest import TestCase
from django.test.client import RequestFactory
from django.core.urlresolvers import reverse
from django.contrib.auth.models import AnonymousUser
from django.core.exceptions import SuspiciousOperation, PermissionDenied

from OWR.users.factory import UserFactory

from .models import OpenHardwareLike
from .views import like_set
from .factory import OpenHardwareFactory


class OpenHardwareViewTests(TestCase):
    BATCH_NUMBER = 10
    def setUp(self):
        self.factory = RequestFactory()
        self.user  = UserFactory()
        self.admin = UserFactory(is_superuser=True, is_staff=True)
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
