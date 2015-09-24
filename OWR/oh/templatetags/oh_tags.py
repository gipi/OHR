from django import template
import logging
from ..models import OpenHardwareLike


logger = logging.getLogger(__name__)

register = template.Library()

@register.assignment_tag
def likes_for_user(user):
    '''
    Assign to a context variable the liked OpenHardware instance
    that the user has favorited.

    Usage

        {% likes_for_user as likes %}
    '''
    return OpenHardwareLike.get_oh_for_user(user)

@register.simple_tag(takes_context=True)
def debug_stocazzo(context, var):
    #print context
    #var = context.get(var, None)
    #import ipdb;ipdb.set_trace()
    logger.debug(var)
    print '#########', var
    return