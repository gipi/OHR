from django.views.decorators.http import require_http_methods
from django.core.exceptions import SuspiciousOperation, PermissionDenied
from django.http import HttpResponse


#@require_http_methods(['POST']) # TODO
import json
from .models import OpenHardwareLike, OpenHardware


import logging


logger = logging.getLogger(__name__)

def like_set(request):
    '''
    Using this view the user sets an OpenHardware instance
    into his favourites.

    The payload has the form

        { 'id': 2, 'action': 'set'}

    This view is available as POST(# TODO) or by AJAX.
    '''
    logger.debug('like_set for %s' % request.user)
    if not request.user.is_authenticated():
        raise PermissionDenied()

    data = None
    pk = None

    actions = {
        'set': lambda pk, user: OpenHardwareLike.objects.create(oh=OpenHardware.objects.get(pk=pk), user=user),
        'unset': lambda pk, user: OpenHardwareLike.objects.filter(oh=OpenHardware.objects.get(pk=pk), user=user).delete(),
    }

    try:
        data = json.loads(request.body)
        pk   = data['id']
        action = data['action']
        actions[action](pk, request.user)
    except Exception as e:
        logger.exception(e)
        raise SuspiciousOperation('JSON data \'%s\' not compliant. user: %s' % (request.body, request.user))

    # place all check before this
    response = {'status': 'ok', 'action': action}

    return HttpResponse(json.dumps(response), content_type='application/json')